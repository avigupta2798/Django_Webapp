# Django_Webapp
A Django Webapp for Authenticating and Signing up users

## Installation
- Create a Virtual Environment for Python3 [venv](https://docs.python.org/3/library/venv.html) for all the libraries.

```bash
python3 -m venv /path/to/new/virtual/environment
```

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.

```bash
pip install -r requirements.txt
```

- Create a Database in MySql

- Change the Database name, username and Password in settings.py file

- Run the manage.py file

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
