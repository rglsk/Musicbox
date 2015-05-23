# Musicbox

## Installation

Note: using `vagrant`

```
$ git clone git@bitbucket.org:progulski/musicbox.git
cd MusicBox/
```

To run vagrant (remember to be in folder with Vagrantfile):

```
vagrant up
```

Enter to vagrant virtual machine:

```
vagrant ssh
cd musicbox/
```

To run stream we need to install and configurate a server. When install choose Yes to configure
it and setup passwords, for host leave default (localhost). 
REMEMBER PASSWORD

```
sudo apt-get install icecast2
musicbox/scripts/setup_icecast2.sh
```

Setup your icecast2 password in deefuzzer.xml:

```
sed -i -e 's/hackme/YOUR_ICECAST2_PASSWORD/g' /home/vagrant/musicbox/deefuzzer.xml
```

Example:

```
sed -i -e 's/hackme/my_new_pass/g' /home/vagrant/musicbox/deefuzzer.xml
```

Run db and stream:

```
musicbox/scripts/setup_tools.sh
```

Before you run application, run tests:

```
nosetests
```

Run musicbox application:

```
cd musicbox/
python app.py
```

Application is available under:

```
127.0.0.1:5000
```

Stream is available under:

```
127.0.0.1:8000/stream.mp3
```



### What I did:

* setup vagrant

* setup mongodb (Why mongo? I never used it, so I thought it'll
  be a good idea to learn a little bit about it)

* backend api using flask and python

* basics tests

* building musicbox python package

* docstrings to generate documentation using Sphinx

* codding python style as it is described in [OpenStack Style Guide](http://docs.openstack.org/developer/hacking/)

* frontend in Bootstrap and jQuery

* setup stream tools (icecast2, defuzzer)

* playing music when user enter the website from moment that song is streamed on server

* user can upload his own music in mp3 format

* when someone upload file every user receive alert that new song has been added (using socketio)

* displaying current song played and playlist (using socketio and thread as a worker:( but about thread later)

* song aren't queued, they are played in alphabetic order (Deefuzzer api dont't give possibility to set it or I couldn't found it)

* read and tested other tools for streaming or APIs like soundcloud, but giveup with them becasue there are authors rights
  and can't upload someones songs



### TODO:

* rewrite all js (it looks very bad)

* better looking frontend (it looks very bad as well)

* do not redirect after file upload

* somehow create queue of songs (probably it can be done parsing xml file with playlist or there is api to do that
  but I havent time for it (I'll check it later for curiosity)

* thred as a worker, instead of this if I had more time I would use Celery

* instead of bash script as provisor in vagrant config there should be used Puppet 

* secure database 



### How it could be expand:

* finish TODO list

* create users

* create more radio stations

* create chat for users 

