# coding: utf-8

from fabric.api import run
from fabric.api import env
from fabric.api import execute
from fabric.decorators import parallel
from fabric.decorators import runs_once

env.hosts = ["192.168.56.101", "192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.command_timeout = 3600
env.keepalive = 60
env.skip_bad_hosts = True
env.timeout = 3


@runs_once
def go_fab():
    result = execute(_go_fab)
    for k, v in sorted(result.iteritems()):
        print "result:", k, v


@parallel
def _go_fab():
    result = []
    result.append(run("hostname"))
    result.append(run("whoami"))
    return result
