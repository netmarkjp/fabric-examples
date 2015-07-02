# coding: utf-8

from fabric.api import run
from fabric.api import env
from fabric.api import settings

env.hosts = ["192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.command_timeout = 1


def go_fab():
    with settings(command_timeout=3):
        run("sleep 2")
        run("echo sleep 2")
        run("sleep 4")
        run("echo sleep 4")
    run("hostname")
    run("whoami")
