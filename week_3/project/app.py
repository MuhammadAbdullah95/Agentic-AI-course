import streamlit as st

# --- Bank Account Class (OOP with Encapsulation) ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


# --- App State (store accounts in memory) ---
if "accounts" not in st.session_state:
    # initialize empty accounts dict in session state
    st.session_state.accounts = {}

st.title("🏦 Simple Banking App")
menu = st.sidebar.selectbox("Menu", ["Create Account", "Deposit", "Withdraw", "Check Balance"])

# --- Create Account ---
if menu == "Create Account":
    st.header("➕ Create a New Bank Account")
    name = st.text_input("Enter account holder name:")
    initial = st.number_input("Initial deposit:", min_value=0, step=100)

    if st.button("Create Account"):
        if name in st.session_state.accounts:
            st.warning("Account already exists!")
        else:
            st.session_state.accounts[name] = BankAccount(name, initial)
            st.success(f"Account created for {name} with balance {initial}")

# --- Deposit Money ---
elif menu == "Deposit":
    st.header("💰 Deposit Money")
    name = st.text_input("Enter account holder name:")
    amount = st.number_input("Enter deposit amount:", min_value=0, step=100)

    if st.button("Deposit"):
        acc = st.session_state.accounts.get(name)
        if acc and acc.deposit(amount):
            st.success(f"Deposited {amount} to {name}. New balance: {acc.get_balance()}")
        else:
            st.error("Account not found or invalid deposit amount.")

# --- Withdraw Money ---
elif menu == "Withdraw":
    st.header("💸 Withdraw Money")
    name = st.text_input("Enter account holder name:")
    amount = st.number_input("Enter withdraw amount:", min_value=0, step=100)

    if st.button("Withdraw"):
        acc = st.session_state.accounts.get(name)
        if acc and acc.withdraw(amount):
            st.success(f"Withdrew {amount} from {name}. New balance: {acc.get_balance()}")
        else:
            st.error("Account not found or insufficient balance.")

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
