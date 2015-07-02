# coding: utf-8

from fabric.api import run
from fabric.api import env

# [gateway:192.168.56.102] -> [dest:192.168.56.102]
env.hosts = ["192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.gateway = "192.168.56.102"


def go_fab():
    run("hostname")
    run("whoami")
    run("w")
