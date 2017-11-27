#!/bin/bash


#chmod +x ./inventory/ec2.py

ANSIBLE_CONFIG=./config/ansible.cfg /usr/local/bin/ansible-playbook -e 'env=AnsibleAWSNginx' task_aws.yml -vvv
