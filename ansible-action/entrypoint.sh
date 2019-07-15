#!/bin/sh -l

cd $GITHUB_WORKSPACE
ansible-playbook $*
