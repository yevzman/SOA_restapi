#!/bin/bash

if [ "$1" == "stop" ]; then
  sudo docker stop postgresql
  sudo docker stop pgadmin
  exit 0
fi
sudo docker compose up -d
sudo docker run --rm --network="postgresql-network" -v "$(pwd)/migrations":/app liquibase/liquibase:4.19.0 --defaultsFile=/app/liquibase.properties update --log-level 1

