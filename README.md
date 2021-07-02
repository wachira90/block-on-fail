# block-on-fail
Security block unwant ssh only

## On root user run by

```
tail -f /var/log/audit/audit.log | python block-ssh.py
```

## Example pattern USER_LOGIN
```
type=USER_LOGIN msg=audit(1624698269.116:20896502): pid=2255 uid=0 auid=4294967295 ses=4294967295 msg='op=login acct="(unknown)" exe="/usr/sbin/sshd" hostname=? addr=218.29.188.139 terminal=ssh res=failed'
```

## Example pattern USER_AUTH
```
type=USER_AUTH msg=audit(1624708006.369:20903329): pid=13129 uid=0 auid=4294967295 ses=4294967295 msg='op=password acct="(unknown)" exe="/usr/sbin/sshd" hostname=? addr=120.201.250.44 terminal=ssh res=failed'
```

## Example pattern CRYPTO_KEY_USER
```
type=CRYPTO_KEY_USER msg=audit(1624708006.632:20903330): pid=13129 uid=0 auid=4294967295 ses=4294967295 msg='op=destroy kind=server fp=SHA256:2a:99:7c:af:38:63:39:45:cc:3c:ac:ad:2d:30:d2:4b:40:bc:4d:7f:1e:a8:93:41:15:91:2d:d9:43:66:ea:b4 direction=? spid=13130 suid=74  exe="/usr/sbin/sshd" hostname=? addr=? terminal=? res=success'
```

## Check Real time add ip
```
tail -f /etc/hosts.deny
```

## crontab remove IP nano /etc/crontab
```
5 4 * * 1  root  /bin/python remove-ip.py
```

### [Mod By => wachira90@yahoo.com]
