# docker-lineage-custom


Steps to build:


- Enable monitor:

`docker compose up -d monitor`


- Change ota server in `docker-compose.yml`


- Build for herolte:

`docker compose up -d build-herolte`


- Check `http://buildserver-ip:3050` for build logs, once sync is finished
