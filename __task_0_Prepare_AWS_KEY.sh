#!/bin/bash


chmod +x ./__task*

ANSIBLE_CONFIG=./config/ansible.cfg /usr/local/bin/ansible-playbook task_prepare.yml
