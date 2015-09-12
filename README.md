Oh Deer - Wildlife Sighting App

Dependancies

    Python 2.7
    Postgres 9.3 + PostGIS
    psycopg2
    Django 1.8

Database setup

The development settings require a Postgres database called "sightings" accessible by user "postgres" that is not password protected. Be sure to add the postGIS extension. From the terminal, run:

createdb -U postgres bikeDB
psql -U postgres -d bikeDB -c "CREATE EXTENSON postgis;"

Syncing the tables from the Django app requires running

./manage.py makemigrations
./manage.py migrate

A full list of required python packages can be found in requirements.txt and can be installed via pip pip install -r requirements.txt

If all dependancies have been met, running ./manage.py runserver should start the development server at 127.0.0.1:8000

Note: There are additional requirements for serving this application in a production setting, and the relevant Django documentation should be consulted in this scenario. This repo does not provide production settings for security reasons.
