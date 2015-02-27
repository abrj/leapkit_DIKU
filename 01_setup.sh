#!/bin/bash

# Install relevent packages

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get build-dep python-imaging
sudo apt-get install vim emacs
sudo apt-get install libjpeg62 libjpeg62-dev
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/libz.so
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/liblibfreetype.so
sudo apt-get install python-pip

sudo pip install -r requirements.txt

cd leapkit
cp leapkit/settings/base_settings_local.py leapkit/settings/base_settings.py
sudo apt-get install python-psycopg2
sudo apt-get install postgresql
