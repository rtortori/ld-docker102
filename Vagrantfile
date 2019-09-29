Vagrant.configure("2") do |config|

  config.vm.define "developer" do |dev|
    dev.vm.box = "ubuntu/bionic64"
    dev.vm.network "forwarded_port", guest: 5000, host: 8181
    dev.vm.network "forwarded_port", guest: 80, host: 8180
    dev.ssh.username = "vagrant"
    dev.vm.hostname = "developer-vm"
    dev.vm.provision "shell", path: "install-docker.sh"
  end

  config.vm.define "production" do |prod|
    prod.vm.box = "ubuntu/bionic64"
    prod.vm.network "forwarded_port", guest: 5000, host: 8280
    prod.ssh.username = "vagrant"
    prod.vm.hostname = "production-vm"
    prod.vm.provision "shell", path: "install-docker.sh"
  end

end
