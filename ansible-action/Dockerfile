FROM python:3.7

LABEL "com.github.actions.name"="Ansible Playbook"
LABEL "com.github.actions.description"="Run an ansible playbook"
LABEL "com.github.actions.icon"="play"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="https://github.com/OpenPrecincts/reforms-microsite"
LABEL "homepage"="https://github.com/OpenPrecincts"
LABEL "maintainer"="Princeton Gerrymandering Project <gerrymander@princeton.edu>"

RUN pip install ansible
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
