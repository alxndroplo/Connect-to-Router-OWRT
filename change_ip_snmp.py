#!/usr/bin/python3
# -*- coding: utf-8 -*-
# SNMP access adress change

import sys
import time
import datetime
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from datetime import datetime
import subprocess
import paramiko
import socket

# ip = "10.116.202.1"
# mip = sys.argv[1]
# mlogin = sys.argv[2]
# mpassword = sys.argv[3]
# mlogin = "root"
# mpassword = "ru17118"


now = datetime.now() 
now_date = now.strftime("%d-%m-%y_%H:%M:%S")
mlogin = "root"
mpassword = "zxcv"


with open('ipaddressd', 'r') as f:
  for mip in f.read().splitlines():
     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     print ("Connect: ",mip, now_date)
     try:
        ssh.connect(mip, port=22, username=mlogin, password=mpassword, timeout=5)
     except (socket.timeout):
        print (f"Превышен интервал подключения к {mip}")
        continue
     except (paramiko.ssh_exception.AuthenticationException):
        print (f"У хоста {mip} другой пароль")
        continue
     stdin, stdout, stderr = ssh.exec_command('''sed -i 's/192.168.2.191/192.168.2.0\/24/g' /etc/config/snmpd''')
     data = stdout.read() + stderr.read()
     print ('Address changet')
     time.sleep(3)
     stdin, stdout, stderr = ssh.exec_command('''/etc/init.d/snmpd restart''')
     data = stdout.read() + stderr.read()
     print ('Restart snmpd - done')
     time.sleep(3)
ssh.close()

