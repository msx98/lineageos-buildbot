# lineageos-buildbot

This repository can be used to build LineageOS for:

- herolte (Galaxy S7) (boots)
- beyond0lte (Galaxy S10e) (untested)

It also provides a preconfigured OTA server, and a monitor for the build process.


## Prerequisites

- I tested this on Debian Buster, make sure you install Docker
- Change the domain name in `.env` into whatever ota domain you intend to work with. Make sure that the releases there are signed with the same key as the build here.
- Create a new network: `docker network create ota`


## Services


### build-herolte

- Image: [lineageos4microg/docker-lineage-cicd](https://github.com/lineageos4microg/docker-lineage-cicd)

- How to use:
  - Run `docker compose up -d build-herolte` in the cloned repository root
  - This initiates the build process. Once the build finishes, the container shuts down. A fresh build, including sync, took me around 24 hours on an i5-2520M with 16GB RAM, Debian Buster (headless). 


### ota-server

- Image: [julianxhokaxhiu/lineageota](https://github.com/julianxhokaxhiu/lineageota)

- How to use:
  - If port 4443 is disabled, install ufw (or your firewall of choice) and run `sudo ufw allow 4443`
  - In docker-compose.yml, replace `../lamp/fs/etc/letsencrypt` with a path to a directory containing: `cert.pem`, `privkey.pem`, `fullchain.pem`
  - Run `docker compose up -d ota-server` in the cloned repository root
  - This will start the OTA server.


### monitor

- Image: [gta98/docker-lineage-monitor](https://github.com/gta98/docker-lineage-monitor)

- How to use:
  - Similarly to ota-server, enable port 3050
  - Run `docker compose up -d monitor` in the cloned respository root
  - Check http://your-address:3050/

## Sync with source

Run: `git submodule update --remote`

## Resolving Issues

- `error: ...: prior sync failed; rebase still in progress`

Can be resolved by running `git am --abort; git reset --hard` in each affected path. There is also `repo forall -c "git am --abort; git reset --hard"` which might take longer.
