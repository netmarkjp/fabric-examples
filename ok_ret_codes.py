# coding: utf-8

from fabric.api import env
from fabric.api import run
from fabric.api import settings

env.hosts = ["192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"


def go_fab():
    with settings(ok_ret_codes=[0, 24]):
        run("exit 0")
        run("exit 24")
    run("hostname")
    run("whoami")
