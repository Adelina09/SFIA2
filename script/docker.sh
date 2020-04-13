#!/bin/bash

source ~/.bashrc
docker stack deploy --compose-file docker_compose.yml stackdemo
