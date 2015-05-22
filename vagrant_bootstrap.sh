#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-pip python-dev python-liblo python-mutagen python-pycurl python-yaml libshout3-dev librtmp-dev liblo-dev libcurl4-openssl-dev
sudo pip install -U distribute setuptools
sudo apt-get install -y git
sudo pip install -e ./musicbox/
