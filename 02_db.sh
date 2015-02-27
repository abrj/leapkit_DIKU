#!/bin/bash

./manage.py syncdb
./manage.py migrate
./manage.py migrate geographic_info
./manage.py migrate institutions
./manage.py migrate projects
./manage.py migrate
