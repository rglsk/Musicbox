Vagrant.configure(2) do |config|
  config.vm.box = 'Debian-jessie-amd64-netboot.box'
  config.vm.box_url = 'https://github.com/holms/vagrant-jessie-box/releases/download/Jessie-v0.1/Debian-jessie-amd64-netboot.box'
  config.vm.provision :shell, path: "vagrant_bootstrap.sh"
  config.vm.synced_folder "./", "/home/vagrant/musicbox"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.network "forwarded_port", guest: 8000, host: 8000
end