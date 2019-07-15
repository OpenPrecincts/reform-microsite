workflow "Deploy On Push" {
  on = "push"
  resolves = [
    "./ansible-action",
    "Only On Master",
  ]
}

action "./ansible-action" {
  uses = "./ansible-action"
  args = "ansible/reform.yml -i ansible/inventory -l reform-auto"
  env = {
    ANSIBLE_GALAXY_FILE = "ansible/requirements.yml"
    ANSIBLE_HOST_KEY_CHECKING = "False"
  }
  secrets = [
    "SECRET_KEY",
    "DATABASE_URL",
    "SMTP_USER",
    "SMTP_PASSWORD",
    "SSH_KEY",
  ]
}

action "Only On Master" {
  uses = "actions/bin/filter@3c0b4f0e63ea54ea5df2914b4fabf383368cd0da"
  args = "branch master"
}
