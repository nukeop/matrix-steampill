# How to run
- Edit config.json, and add your server's https address, and the application service token
- Edit steam-registration.yaml, setting up the id, tokens, url of the steampill bridge server you'll be running it on, etc
- `$ virtualenv -p python3 venv`
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`
- `$ python run.py`

The bridge will log to steampill.log until it reaches 2MB in size, then it will rotate the logs between 3 files. It also outputs everything to the terminal.
