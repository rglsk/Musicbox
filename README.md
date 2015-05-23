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

Run musicbox application:

```
cd musicbox/
python app.py
```

Application is avaible under:

```
127.0.0.1:5000
```

Stream is avaible under:

```
127.0.0.1:8000/stream.mp3
```