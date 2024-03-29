# OKBatchTracker

This app will be used by Oregon Kombucha customers to track the progress of thier kombuca batches as they brew.

## Local setup
After cloning the repo, run `python -m virtualenv venv` to create a new virtual environment.  

Next run `source ./venv/bin/activate` to activate the new environment.

Run `pip install --upgrade pip` to ensure you are using the latest python package manager.

Finally run `pip install -r requirements.txt` to install all needed packages.

## Running the app locally

After completing local setup, run `python manage.py migrate` to create and setup the database, then `python manage.py runserver` to start the server.  Navigate to 127.0.0.1:8000 in your web browser to view the app.

## Running tests

Run `python manage.py migrate` to create and setup the database, then `python manage.py test` to run tests.
