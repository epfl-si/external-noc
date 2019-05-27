#!/bin/bash
#Petit script pour installer tout le binz
#zf190527.1524



sudo apt update
sudo apt install -y python3 python3-pip hiera-eyaml
sudo -H pip3 install ansible bcrypt

#nano ansible/keys/private_key.pkcs7.pem

