#!/bin/bash

chmod +x ./DynamicInventory/ec2.py

ANSIBLE_CONFIG=./config/ansible_ec2.cfg /usr/local/bin/ansible-playbook  task_Codecom.yml
