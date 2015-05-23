#!/usr/bin/env bash

sudo sed -i -e 's/ENABLE=false/ENABLE=true/g' /etc/default/icecast2
sudo /etc/init.d/icecast2 restart