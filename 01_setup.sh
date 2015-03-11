#!/bin/bash

# update base system.
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

# Install dependencies
sudo apt-get build-dep python-imaging
sudo apt-get install vim emacs libjpeg62 libjpeg62-dev python-pip python-psycopg2 postgresql

# Do magic linking.
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/libz.so
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/liblibfreetype.so

# Install leapkit specific packages from pip.
sudo pip install -r requirements.txt

# Change to correct working directory and apply django settings.
cd leapkit
cp leapkit/settings/base_settings_local.py leapkit/settings/base_settings.py
