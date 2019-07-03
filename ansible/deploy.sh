#!/bin/bash

ansible-playbook ansible/reform.yml -i reform.openprecincts.org, -u emergency -e ansible_ssh_password=$ANSIBLE_SSH_PASS
