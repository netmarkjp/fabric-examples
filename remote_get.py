# coding: utf-8

from fabric.api import run
from fabric.api import env
from fabric.api import get

env.hosts = ["192.168.56.101", "192.168.56.102", "192.168.56.103"]
env.user = "user0"
env.password = "password0"
env.command_timeout = 3600
env.keepalive = 60
env.skip_bad_hosts = True
env.timeout = 3
env.parallel = True


def go_fab():
    temp = run("mktemp")
    run("for i in {1..10000}; do echo $RANDOM >>%s ; done" % (temp))
    run("hostname >>%s" % (temp))
    run("whoami >>%s" % (temp))

    # 取得後のファイルパスを指定する場合は第二引数を指定。
    # 例:           get(temp, "/tmp/%s.log" % (env.host_string))
    # デフォルト:   env.host_string/取得元と同じファイル名 (ディレクトリは自動作成される)
    get(temp)
