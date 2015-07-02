# coding: utf-8

from fabric.api import run
from fabric.api import env

env.hosts = ["192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.parallel = True


def go_fab():
    run("hostname")
    run("whoami")
