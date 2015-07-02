Macの場合、 ``fab`` のところは ``SSH_AUTH_SOCK= fab`` とする必要あるかも。


# 複数のサーバに対して同じユーザ・パスワードでログインする

```
fab -f set_hosts_password.py go_fab
```

[set_hosts_password.py](set_hosts_password.py)

# 複数のサーバに対してそれぞれ異なるユーザ・パスワードでログインする

```
fab -f set_hosts_passwords.py go_fab
```

# コマンド実行成功と判断するコマンドのリターンコードを指定する

```
fab -f ok_ret_codes.py go_fab
```

# 必ず並列実行する

```
fab -f parallel.py go_fab
```

# sshのconfigを使う

```
fab -f ssh_config.py go_fab
```

# 踏み台経由でSSHする

```
fab -f gateway.py go_fab
```

# SSHでつながらないホストは無視する

```
fab -f skip_bad_hosts.py go_fab
```

# コマンド実行のタイムアウトを指定する

```
fab -f command_timeout.py go_fab
```

# SSH接続キープアライブを設定する

```
fab -f keepalive.py go_fab
```

# 並列実行した結果を接続先ホストごとにまとめる

```
fab -f perhostresult.py go_fab
```

# リモートで実行した大量の結果を接続先ホストごとにまとめて手元に持ってくる

```
fab -f remote_get.py go_fab
```

