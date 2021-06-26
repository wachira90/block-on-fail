import sys
import re

while True:
    line = sys.stdin.readline()
    k = line.split()
    if (re.findall("USER_LOGIN", k[0])):
        print("OK CASE USER_LOGIN")
        if (re.findall("unknown", k[7]) or re.findall("root", k[7])):
            print("OK CASE unknown root")
            ip = k[10].split("=")[1].replace(" ","")
            print("OK BLOCK => ",ip)
            res = "sshd:" + ip + "\n"
            f = open("/etc/hosts.deny","a")
            f.write(res)
            f.close()
            print(res)
    else:
        print("NO CASE")
