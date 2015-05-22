#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-pip python-dev python-liblo python-mutagen python-pycurl python-yaml libshout3-dev librtmp-dev liblo-dev libcurl4-openssl-dev
sudo pip install -U distribute setuptools
sudo apt-get install -y git
sudo pip install -e ./musicbox/
sudo pip install deefuzzer
sudo apt-get install --assume-yes icecast2
sudo sed -i -e 's/ENABLE=false/ENABLE=true/g' /etc/default/icecast2
sudo /etc/init.d/icecast2 restart
sudo sed -i -e 's/ssl_version=PROTOCOL_SSLv3/ssl_version=PROTOCOL_SSLv23/g' /usr/local/lib/python2.7/dist-packages/gevent/ssl.py