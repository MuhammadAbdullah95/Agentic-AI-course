# Simple Banking Streamlit App (Educational)

This small demo implements a minimal banking app using Streamlit to
illustrate OOP concepts (encapsulation), file persistence, and a
very small user interface.

What you'll find
- `app.py`  : Simplified Streamlit front-end (in-memory session state)
- `app2.py` : More complete app with file-based persistence (`accounts.json`)
- `accounts.json` : Data file used by `app2.py` (created at runtime)

How to run
1. Create a virtual environment with Python 3.11+ and install requirements:
```powershell
	 python -m venv .venv
	 .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt
```
2. Run the app:

	 streamlit run app2.py

Alternative: use `uv` (a lightweight workflow helper included in this course)

If your environment provides the `uv` helper, these are the common commands
used in this project (Windows):

1. Create a venv managed by `uv` (this initializes a local `.venv`):

```powershell
uv venv
```

2. Activate the created virtual environment (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
# or if the helper created a different activate script
.venv\Scripts\activate
```

3. Sync dependencies (install from requirements or uv lock file):

```powershell
uv sync
```

4. Run the Streamlit apps using `uv` shortcuts or directly:

```powershell
# Run app.py using streamlit directly
streamlit run app.py

# Or use uv to run Streamlit for app2
uv run streamlit run app2.py
```

Notes:
- `uv` is used in this repository as a convenience wrapper — if you don't
	have it installed, use the `python -m venv` and `pip install -r requirements.txt` steps above.
- The commands above assume a Windows PowerShell environment; adapt the
	activate command for other shells (macOS/Linux: `source .venv/bin/activate`).

Notes for students
- The project demonstrates a simple BankAccount class that keeps the
	balance private and exposes deposit/withdraw methods.
- `app2.py` shows defensive file handling: it backs up corrupt JSON and
	validates input before changing balances.
- This is a learning project: the PINs are stored in plain text and the
	code is not production-ready. Focus on understanding the OOP patterns
	and how Streamlit session state is used.

Extending the demo
- Add unit tests for `BankAccount` and the file helpers (start small).
- Replace plain-text PINs with a hashing function (bcrypt) and compare flows.
