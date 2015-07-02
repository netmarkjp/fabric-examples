# coding: utf-8

from fabric.api import run
from fabric.api import env
from fabric.api import execute

env.user = "user0"
env.password = "password0"
env.command_timeout = 3600
env.keepalive = 60
env.skip_bad_hosts = True
env.timeout = 3
env.parallel = True


def go_fab():
    result = execute(
        _go_fab, hosts=["192.168.56.101", "192.168.56.102", "192.168.56.103"])
    execute(print_result, result, hosts=[])


def _go_fab():
    result = []
    result.append(run("hostname"))
    result.append(run("whoami"))
    return result


def print_result(results):
    for k, v in sorted(results.iteritems()):
        print "result:", k, v
