# coding: utf-8

from fabric.api import run
from fabric.api import env

env.hosts = ["192.168.56.102", "192.168.56.103"]
env.password = "password0"
env.ssh_config_path = "config.local"
env.use_ssh_config = True


def go_fab():
    run("hostname")
    run("whoami")
