workflow "New workflow" {
  on = "push"
  resolves = ["./ansible-action"]
}

action "./ansible-action" {
  uses = "./ansible-action"
  args = "ansible/reform.yml -i ansible/inventory -l reform-auto"
  env = {
    ANSIBLE_GALAXY_FILE = "ansible/requirements.yml"
  }
  secrets = ["SECRET_KEY", "DATABASE_URL", "SMTP_USER", "SMTP_PASSWORD"]
}
