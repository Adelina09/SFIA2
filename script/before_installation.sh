#!/bin/bash

#install python3 and pip

apt install -y python 

apt install -y python-pip

# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
touch ~/.bashrc
echo 'PATH=$PATH:~/.local/bin' > ~/.bashrc
## change ownership
sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc
## install ansible with pip
pip install --user ansible
# check that ansible has been installed
ansible --version

