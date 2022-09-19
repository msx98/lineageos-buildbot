# lineageos-buildbot

This repository can be used to build LineageOS for:

- herolte (Galaxy S7) (boots)
- beyond0lte (Galaxy S10e) (untested)

It also provides a preconfigured OTA server, and a monitor for the build process.


## Prerequisites

I tested this on Debian Buster, make sure you install Docker


## Services


### build-herolte

- Image: [lineageos4microg/docker-lineage-cicd](https://github.com/lineageos4microg/docker-lineage-cicd)

- How to use:
  - Inside docker-compose.yml, change OTA_SERVER to your own address.
  - Run `docker compose up -d build-herolte` in the cloned repository root
  - This initiates the build process. Once the build finishes, the container shuts down. A fresh build, including sync, took me around 24 hours on an i5-2520M with 16GB RAM, Debian Buster (headless). 


### ota-server

- Image: [julianxhokaxhiu/lineageota](https://github.com/julianxhokaxhiu/lineageota)

- How to use:

  - Run `docker compose up -d ota-server` in the cloned repository root
  - This will start the OTA server.


### monitor

- Image: [gta98/docker-lineage-monitor](https://github.com/gta98/docker-lineage-monitor)

- How to use:
  - Run `docker compose up -d monitor` in the cloned respository root
  - Check http://your-address:3050/
