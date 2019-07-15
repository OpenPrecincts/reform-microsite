workflow "New workflow" {
  on = "push"
  resolves = ["./ansible-action"]
}

action "./ansible-action" {
  uses = "./ansible-action"
  args = "ansible/reform.yml"
}
