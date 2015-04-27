#!/bin/bash

# update base system.
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade

# Install dependencies
sudo apt-get -y install build-dep python-imaging
sudo apt-get -y install libjpeg62 libjpeg62-dev python-pip python-psycopg2 postgresql

# Do magic linking.
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/libz.so
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/liblibfreetype.so

# Install leapkit specific packages from pip.
sudo pip install -ry requirements.txt

# Change to correct working directory and apply django settings.
cd leapkit
cp leapkit/settings/base_settings_local.py leapkit/settings/base_settings.py
