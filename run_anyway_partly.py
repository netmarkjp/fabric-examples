# coding: utf-8

from fabric.api import env
from fabric.api import run
from fabric.api import settings

env.hosts = ["192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"


def go_fab():
    with settings(warn_only=True):
        run("ls /none")
    run("hostname")
    run("whoami")
