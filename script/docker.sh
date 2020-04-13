#!/bin/bash

source ~/.bashrc
sudo docker stack deploy --compose-file docker_compose.yml stackdemo
