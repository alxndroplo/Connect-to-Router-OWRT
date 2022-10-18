#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


with open('zbx_export_hosts (1).json', 'r',) as f:
    data = json.load (f)
    #print (type(data))
    for item in data ['zabbix_export'] ['hosts']:
#        print (type(item['interfaces']))
        for ip in item ['interfaces'] :
#              print (ip['ip'])
              file1 = (ip['ip'])
              print (file1)
            #   with open ('ipaddress.txt', 'w') as file:
            #     for line in file1:
            #         file.write(line + '\n')