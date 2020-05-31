# Setup
Ensure you havegot Python >= 3.6 installed.

pip-install all required libraries on `requirements.txt` with the command:
`pip install -r requirements.txt`

# Run
Entry point is main.py, just run this with
`python main.py`

## Adding widgets
Add a QWidget subclass under `./ui` submodule. Do not forget to import it under `ui/__init__.py` in order to adhere to python module best practises.