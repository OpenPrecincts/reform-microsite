#!/bin/sh -l

mkdir ~/.ssh/
echo $SSH_KEY > ~/.ssh/id_rsa

cd $GITHUB_WORKSPACE
ansible-galaxy install -r $ANSIBLE_GALAXY_FILE
ansible-playbook $*
