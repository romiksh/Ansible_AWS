#!/bin/bash

ANSIBLE_CONFIG=./config/ansible.cfg /usr/local/bin/ansible-playbook -e 'env=Docker_ECS' task_docker_wrong.yml
