# coding: utf-8

from fabric.api import run
from fabric.api import env

env.hosts = ["192.168.56.101", "192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.command_timeout = 90
env.keepalive = 60
env.skip_bad_hosts = True
env.timeout = 3

results = {}
for h in env.hosts:
    results[h] = []


def go_fab():
    _go_fab()
    for k, v in sorted(results.iteritems()):
        print "results:", k, v


def _go_fab():
    result = []
    result.append(run("hostname"))
    result.append(run("whoami"))
    results[env.host_string].append(result)
