#!/bin/bash

sudo -u jenkins aws configure
sudo -u jenkins git config --global credential.helper '!aws codecommit credential-helper $@'
sudo -u jenkins git config --global credential.useHttpPath true


chmod +x ./DynamicInventory/ec2.py
ANSIBLE_CONFIG=./config/ansible_ec2.cfg /usr/local/bin/ansible-playbook  task_prepare_codedeploy.yml
