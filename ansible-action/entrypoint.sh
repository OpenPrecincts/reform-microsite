#!/bin/sh -l

cd $GITHUB_WORKSPACE
ansible-galaxy install -r $ANSIBLE_GALAXY_FILE
ansible-playbook $*
