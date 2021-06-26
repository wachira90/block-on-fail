#!python
import re

file = "/etc/hosts.deny"

a_file = open(file, "r")
lines = a_file.readlines()
a_file.close()

new_file = open(file, "w+")
for line in lines:
    if not re.findall("sshd", line):
        new_file.write(line)
        print('NO => ',line)

new_file.close()
