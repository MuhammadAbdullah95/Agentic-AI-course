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

	 python -m venv .venv
	 .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt

2. Run the app:

	 streamlit run app2.py

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
