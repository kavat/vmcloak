VMCloak
=======

Automated Virtual Machine Generation and Cloaking for Cuckoo Sandbox.

Introduction
------------

VMCloak is a tool to fully create and prepare Virtual Machines that can be
used by Cuckoo Sandbox. In order to create a new Virtual Machine one should
prepare a few configuration values that will be used later on by the tool.

Dependencies
------------

* Docker
* Docker compose
* At least GB required for HD (minimum 20)
* Access to host /dev/kvm device

Starting services
-----------------

Simple docker compose start command creates architecture

```
docker-compose up -d --remove-orphans
```

First configuration
-------------------

* Database

```
docker exec -it guac-db /bin/bash
cat /tmp/templates/* | mysql -u root -puser_root_password guacamole_db
```

First image building
--------------------

```
docker exec -it vmcloak /bin/bash
chmod 666 /dev/kvm
vmcloak-qemubridge br0 192.168.30.1/24
vmcloak isodownload --win10x64 --download-to /root/iso/win10x64.iso
mkdir /mnt/win10x64
mount -o loop,ro /root/iso/win10x64.iso /mnt/win10x64
vmcloak --debug init --win10x64 --hddsize 50 --cpus 2 --ramsize 4096 --network 192.168.30.0/24 --vm qemu --ip 192.168.30.2 --iso-mount /mnt/win10x64 win10base br0
vmcloak --debug install win10base tightvnc dotnet:3.5 dotnet:4.7.2 java:8u151 vcredist:2013 vcredist:2019 carootcert firefox wallpaper uninstallsw disableservices
```
