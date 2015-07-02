# coding: utf-8

from fabric.api import run
from fabric.api import env

env.hosts = ["user1@192.168.56.102", "user2@192.168.56.103"]
env.passwords = {"user1@192.168.56.102:22": "password1",
                 "user2@192.168.56.103:22": "password2", }


def go_fab():
    run("hostname")
    run("whoami")
