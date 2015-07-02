Macの場合、 ``fab`` のところは ``SSH_AUTH_SOCK= fab`` とする必要あるかも。


# 複数のサーバに対して同じユーザ・パスワードでログインする

[set_hosts_password.py](set_hosts_password.py)

```
fab -f set_hosts_password.py go_fab
```

# 複数のサーバに対してそれぞれ異なるユーザ・パスワードでログインする

[set_hosts_passwords.py](set_hosts_passwords.py)

```
fab -f set_hosts_passwords.py go_fab
```

# コマンド実行成功と判断するコマンドのリターンコードを指定する

[ok_ret_codes.py](ok_ret_codes.py)

```
fab -f ok_ret_codes.py go_fab
```

# 必ず並列実行する

[parallel.py](parallel.py)

```
fab -f parallel.py go_fab
```

# sshのconfigを使う

[ssh_config.py](ssh_config.py)

```
fab -f ssh_config.py go_fab
```

# 踏み台経由でSSHする

[gateway.py](gateway.py)

```
fab -f gateway.py go_fab
```

# SSHでつながらないホストは無視する

[skip_bad_hosts.py](skip_bad_hosts.py)

```
fab -f skip_bad_hosts.py go_fab
```

# コマンド実行のタイムアウトを指定する

[command_timeout.py](command_timeout.py)

```
fab -f command_timeout.py go_fab
```

# SSH接続キープアライブを設定する

[keepalive.py](keepalive.py)

```
fab -f keepalive.py go_fab
```

# 並列実行した結果を接続先ホストごとにまとめる

[perhostresult.py](perhostresult.py)

```
fab -f perhostresult.py go_fab
```

# リモートで実行した大量の結果を接続先ホストごとにまとめて手元に持ってくる

[remote_get.py](remote_get.py)

```
fab -f remote_get.py go_fab
```

