import streamlit as st
import json
import os
import time

# --- File Handling Functions ---
# Use a deterministic path relative to this file so the app behaves the same
# regardless of the current working directory when Streamlit runs.
BASE_DIR = os.path.dirname(__file__)
FILE = os.path.join(BASE_DIR, "accounts.json")

def load_accounts():
    """Load accounts from FILE.

    Returns a dict mapping account name -> BankAccount.
    If the file is missing, empty, or corrupt we return an empty dict. In the
    case of corrupt JSON we attempt to back up the bad file so the user can
    inspect it.
    """
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # empty file -> treat as no accounts
        if not content or not content.strip():
            return {}

        data = json.loads(content)

        if not isinstance(data, dict):
            st.warning("accounts.json does not contain the expected object; starting with no accounts.")
            return {}

        # convert dictionary back into BankAccount objects
        result = {}
        for name, info in data.items():
            balance = info.get("balance", 0)
            pin = info.get("pin")
            transactions = info.get("transactions", [])
            result[name] = BankAccount(name, balance, pin, transactions)
        return result

    except json.decoder.JSONDecodeError:
        # backup the corrupted file so we don't lose data and start fresh
        timestamp = int(time.time())
        backup_path = f"{FILE}.corrupt.{timestamp}.bak"
        try:
            os.replace(FILE, backup_path)
            st.warning(f"accounts.json is corrupted and was moved to {os.path.basename(backup_path)}. Starting with an empty account list.")
        except (OSError, PermissionError) as err:
            st.error(f"accounts.json is corrupted and could not be backed up: {err}. Starting with an empty account list.")
        return {}

    except (OSError, PermissionError) as e:
        st.error(f"Unable to read accounts file: {e}")
        return {}

    except UnicodeError as e:
        st.error(f"Unable to decode accounts file (encoding issue): {e}")
        return {}

def save_accounts(accounts):
    """Persist accounts to FILE. Returns True on success, False on error."""
    data = {}
    for name, acc in accounts.items():
        data[name] = {
            "balance": acc.get_balance(),
            "pin": getattr(acc, "pin", None),
            "transactions": getattr(acc, "_transactions", []),
        }

    # ensure directory exists (should already, but be defensive)
    try:
        os.makedirs(os.path.dirname(FILE), exist_ok=True)
    except OSError:
        # if we can't create dirs, we still attempt to write and let that fail
        pass

    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except (OSError, PermissionError) as e:
        st.error(f"Failed to save accounts: {e}")
        return False
    except TypeError as e:
        st.error(f"Failed to serialize accounts data: {e}")
        return False


def transfer(from_acc, to_acc, amt):
    """Transfer amt from from_acc to to_acc. Returns True on success."""
    if from_acc is None or to_acc is None:
        return False
    if amt <= 0:
        return False
    if from_acc.get_balance() < amt:
        return False

    # perform
    from_acc.withdraw(amt)
    to_acc.deposit(amt)
    from_acc.add_transaction("transfer_out", amt, details={"to": to_acc.owner})
    to_acc.add_transaction("transfer_in", amt, details={"from": from_acc.owner})
    return True



# --- Bank Account Class (OOP + Encapsulation) ---
class BankAccount:
    def __init__(self, owner, balance=0, pin=None, transactions=None):
        self.owner = owner
        self.__balance = balance   # private attribute
        # Simple PIN for demo purposes (not secure storage)
        self.pin = pin
        # transactions is a list of dicts: {ts, type, amount, details}
        self._transactions = transactions or []

    def _now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def add_transaction(self, ttype, amt, details=None):
        entry = {"ts": self._now(), "type": ttype, "amount": amt, "details": details}
        self._transactions.append(entry)

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            self.add_transaction("deposit", amt)
            return True
        return False

    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
            self.add_transaction("withdraw", amt)
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_statement(self, limit=None):
        if limit:
            return list(self._transactions[-limit:])
        return list(self._transactions)

    def set_pin(self, new_pin):
        self.pin = new_pin


# --- App State (load from file on first run) ---
if "accounts" not in st.session_state:
    st.session_state.accounts = load_accounts()

st.title("🏦 Simple Banking App (demo)")
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Transfer",
        "Check Balance",
        "Statement",
        "List Accounts",
        "Settings",
    ],
)

# --- Create Account ---
if menu == "Create Account":
    st.header("➕ Create a New Bank Account")
    name = st.text_input("Enter account holder name:")
    initial = st.number_input("Initial deposit:", min_value=0, step=100)
    pin_input = st.text_input("Set PIN (numbers or text):", type="password")

    if st.button("Create Account"):
        if name in st.session_state.accounts:
            st.warning("Account already exists!")
        else:
            st.session_state.accounts[name] = BankAccount(name, initial, pin_input or None)
            save_accounts(st.session_state.accounts)
            st.success(f"Account created for {name} with balance {initial}")

# --- Deposit Money ---
elif menu == "Deposit":
    st.header("💰 Deposit Money")
    name = st.text_input("Enter account holder name:")
    amount = st.number_input("Enter deposit amount:", min_value=0, step=100)

    if st.button("Deposit"):
        acc = st.session_state.accounts.get(name)
        if acc and acc.deposit(amount):
            save_accounts(st.session_state.accounts)
            st.success(f"Deposited {amount} to {name}. New balance: {acc.get_balance()}")
        else:
            st.error("Account not found or invalid deposit amount.")

# --- Withdraw Money ---
elif menu == "Withdraw":
    st.header("💸 Withdraw Money")
    name = st.text_input("Enter account holder name:")
    amount = st.number_input("Enter withdraw amount:", min_value=0, step=100)

    pin = st.text_input("Enter PIN:", type="password")
    if st.button("Withdraw"):
        acc = st.session_state.accounts.get(name)
        if not acc:
            st.error("Account not found.")
        else:
            if acc.pin is None:
                st.error("Account has no PIN set. Please set a PIN in Settings before withdrawing.")
            elif pin != acc.pin:
                st.error("Invalid PIN.")
            elif acc.withdraw(amount):
                save_accounts(st.session_state.accounts)
                st.success(f"Withdrew {amount} from {name}. New balance: {acc.get_balance()}")
            else:
                st.error("Insufficient balance or invalid amount.")

# --- Transfer ---
elif menu == "Transfer":
    st.header("🔁 Transfer Money")
    from_name = st.text_input("From account:")
    to_name = st.text_input("To account:")
    amount = st.number_input("Amount:", min_value=0, step=100)
    from_pin = st.text_input("From account PIN:", type="password")

    if st.button("Transfer"):
        from_acc = st.session_state.accounts.get(from_name)
        to_acc = st.session_state.accounts.get(to_name)
        if not from_acc or not to_acc:
            st.error("One or both accounts not found.")
        elif from_acc.pin is None:
            st.error("Source account has no PIN set. Please set a PIN in Settings before transferring.")
        elif from_pin != from_acc.pin:
            st.error("Invalid PIN for source account.")
        elif transfer(from_acc, to_acc, amount):
            save_accounts(st.session_state.accounts)
            st.success(f"Transferred {amount} from {from_name} to {to_name}.")
        else:
            st.error("Transfer failed (invalid amount or insufficient funds).")

# --- Check Balance ---
elif menu == "Check Balance":
    st.header("📊 Check Account Balance")
    name = st.text_input("Enter account holder name:")

    if st.button("Check Balance"):
        acc = st.session_state.accounts.get(name)
        if acc:
            st.info(f"Account: {name} | Balance: {acc.get_balance()}")
        else:
            st.error("Account not found.")

# --- Statement ---
elif menu == "Statement":
    st.header("📄 Account Statement")
    name = st.text_input("Enter account holder name:")
    limit = st.number_input("Show last N transactions (0 = all):", min_value=0, value=10)

    pin = st.text_input("Enter PIN:", type="password")
    if st.button("Show Statement"):
        acc = st.session_state.accounts.get(name)
        if not acc:
            st.error("Account not found.")
        elif acc.pin is None:
            st.error("Account has no PIN set. Please set a PIN in Settings to view statements.")
        elif pin != acc.pin:
            st.error("Invalid PIN.")
        else:
            rows = acc.get_statement(None if limit == 0 else limit)
            if not rows:
                st.info("No transactions yet.")
            else:
                for r in rows:
                    st.write(f"{r['ts']} | {r['type']} | {r['amount']} | {r.get('details')}")

# --- List Accounts ---
elif menu == "List Accounts":
    st.header("📋 All Accounts")
    if not st.session_state.accounts:
        st.info("No accounts available.")
    else:
        for name, acc in st.session_state.accounts.items():
            st.write(f"{name} — Balance: {acc.get_balance()}")

# --- Settings ---
elif menu == "Settings":
    st.header("⚙️ Account Settings")
    name = st.text_input("Account name for settings:")
    old_pin = st.text_input("Current PIN (required to change):", type="password")
    new_pin = st.text_input("New PIN (leave blank to skip):", type="password")

    if st.button("Update Settings"):
        acc = st.session_state.accounts.get(name)
        if not acc:
            st.error("Account not found.")
        else:
            # If an account already has a PIN, require the old one to change it
            if acc.pin is not None:
                if not old_pin:
                    st.error("Please enter current PIN to change it.")
                elif old_pin != acc.pin:
                    st.error("Current PIN is incorrect.")
                elif new_pin:
                    acc.set_pin(new_pin)
                    save_accounts(st.session_state.accounts)
                    st.success("PIN updated.")
                else:
                    st.info("No changes applied.")
            else:
                # No existing PIN — allow set without old PIN
                if new_pin:
                    acc.set_pin(new_pin)
                    save_accounts(st.session_state.accounts)
                    st.success("PIN set for account.")
                else:
                    st.info("No changes applied.")
