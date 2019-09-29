# 2. Learn and Do: Docker 102
#### A "Learn and do" series for people exploring Docker containers for the very first time 
###### Cisco Italy Multicloud Users Meetup
<hr>

#### Prerequisites

Prerequisites from [Docker primer Learn and Do](https://github.com/rtortori/ld-dockerprimer):

* Windows, MacOS or Linux
* [Install Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* [Install Git](https://git-scm.com/downloads)

Additional prerequisites for this Learn and Do:

* [Create a free account on Docker Hub](https://hub.docker.com)
* \[Optional\] An advanced text editor like [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/), or [Notepad ++](https://notepad-plus-plus.org/)

#### Introduction

In the [first episode](https://github.com/rtortori/ld-dockerprimer) we had a quick bite at Docker containers.<br>
We've seen how and why they are so flexible and... 

We are going to run two labs in this Learn and Do:

* Build container images
* Container image structure and user capabilities

Let's get started. 

#### Build container images (~20 minutes to complete)

docker hub
cloen repo
containerize & dockerfile
tag push
run in prod





One of the most interesting element introduced by Docker is [Docker Hub](https://hub.docker.com), a public image [registry](https://docs.docker.com/registry/) which allows users to upload and share docker images. On Docker Hub, you can also find official images from IT vendors, which are validated by Docker as genuine images.

#### Container image structure and user capabilities (~15 minutes to complete)



busybox exa -> image struct
create and rm file
layer struct
use capa

docker compese




Quote:
>Containerization is increasingly popular because containers are:

>* Flexible: Even the most complex applications can be containerized.
>* Lightweight: Containers leverage and share the host kernel.
>* Interchangeable: You can deploy updates and upgrades on-the-fly.
>* Portable: You can build locally, deploy to the cloud, and run anywhere.
>* Scalable: You can increase and automatically distribute container replicas.
>* Stackable: You can stack services vertically and on-the-fly.

[link](https://www.docker.com/resources/what-container)

#### Prerequisites

* Windows, MacOS or Linux
* [Install Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* [Install Git](https://git-scm.com/downloads)

#### Preparation activities

Code:

```bash
git clone https://github.com/rtortori/ld-dockerprimer.git
```

Hide code:
<details>
    <summary>Sample Output</summary>
    <pre>
➜  dockerprimer git:(master) > vagrant up
Bringing machine 'developer' up with 'virtualbox' provider...
Bringing machine 'production' up with 'virtualbox' provider...
==> developer: Importing base box 'ubuntu/bionic64'...
==> developer: Matching MAC address for NAT networking...
==> developer: Checking if box 'ubuntu/bionic64' version '20190612.0.0' is up to date...
==> developer: Setting the name of the VM: dockerprimer_developer_1568963962471_12169
==> developer: Clearing any previously set network interfaces...
==> developer: Preparing network interfaces based on configuration...
    developer: Adapter 1: nat
==> developer: Forwarding ports...
    developer: 5000 (guest) => 8180 (host) (adapter 1)
    developer: 22 (guest) => 2222 (host) (adapter 1)
==> developer: Running 'pre-boot' VM customizations...
==> developer: Booting VM...
==> developer: Waiting for machine to boot. This may take a few minutes...
    developer: SSH address: 127.0.0.1:2222
[...]
production: Setting up docker-ce (5:19.03.2~3-0~ubuntu-bionic) ...
    production: Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
    production: Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
    production: Processing triggers for ureadahead (0.100.0-21) ...
    production: Processing triggers for libc-bin (2.27-3ubuntu1) ...
    production: Processing triggers for systemd (237-3ubuntu10.22) ...
    </pre>
    </details>
    
*italic*

Table:

| Parameter     | Meaning                                 |
| ------------- |-----------------------------------------|
| run           | Create a new container                  |
| -it           | Attach a terminal and allow interaction |
| centos        | The image used                          |
| bash          | The process to execute                  |


Image:
![NGINX Landing Page](https://raw.githubusercontent.com/rtortori/ld-)