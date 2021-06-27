#!python3
import sys
import re
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("-n", "--name", required=True)
parser.add_argument("--cmd", required=True)
args = parser.parse_args()

'''
# FIND KILL PROCESS
ps -aux | grep -i tail

# KILL PROCESS
kill -9 <pid-number>

# FOR START BLOCK 
tail -f /var/log/audit/audit.log | python3 block-on-fail.py --cmd block &>/dev/null &

tail -f /var/log/audit/audit.log | python3 block-on-fail.py --cmd block /dev/null 2>&1 &

[root@bma-por ~]# tail -f /var/log/audit/audit.log | python3 block-on-fail.py --cmd block > /dev/null 2>&1 &
[1] 7125
[root@bma-por ~]#

# FOR START REMOVE LIST IN CRONTAB
python3 block-on-fail.py --cmd remove

# crontab -e
5 4 */3 * * /bin/python3 block-on-fail.py --cmd remove
5 4 */3 * *  $(which python3)  block-on-fail.py --cmd remove

# START SERVICE
python3 block-on-fail.py --cmd start

# STOP SERVICE
python3 block-on-fail.py --cmd stop

# SHOW BLOCK IP
python3 block-on-fail.py --cmd show
'''

def mode_block_user_login(): # BLOCK USER_LOGIN
    print('MODE BLOCK')
    while True:
        line = sys.stdin.readline()
        k = line.split()
        if (re.findall("USER_LOGIN", k[0])):
            print("OK CASE => USER_LOGIN")
            if (re.findall("unknown", k[7]) or re.findall("root", k[7])):
                print("OK CASE => unknown root")
                ip = k[10].split("=")[1].replace(" ","")
                print("OK BLOCK => ",ip)
                res = "sshd:" + ip + "\n"
                f = open("/etc/hosts.deny","a")
                f.write(res)
                f.close()
                print(res)
        else:
            print("NO CASE")

def mode_remove(): # REMOVE IP
    print('MODE REMOVE')
    file = "/etc/hosts.deny"
    a_file = open(file, "r")
    lines = a_file.readlines()
    a_file.close()
    new_file = open(file, "w+")
    for line in lines:
        if not re.findall("sshd", line):
            new_file.write(line)
        else:
            print('REMOVE IP : ',line)
    new_file.close()

if (args.cmd == 'block'):
    print(f'COMMAND {args.cmd} STARTED')
    mode_block_user_login()
elif (args.cmd == 'remove'):
    print(f'COMMAND {args.cmd} STARTED')
    mode_remove()
else:
    print('NO COMMAND')
