#!/bin/bash
# Change to the correct working directory
cd leapkit/

# Sync the database model (Django analyses classes and creates it's own models.)
./manage.py syncdb

# Migrate the created models to the SQL database.
./manage.py migrate

# Some models won't migrate because of relations, migrate in specific order to fix.
./manage.py migrate geographic_info
./manage.py migrate institutions
./manage.py migrate projects
./manage.py migrate

# for our own linkedin tables.
./manage.py syncdb --all
