#!/usr/bin/env python

import requests

headers = {"Cookie":"WC=10544494-0-ooAmppgcza7CrmQ1"}
res = requests.get('http://www.wechall.net/challenge/training/programming1/index.php?action=request',
   headers=headers)

#print res.headers
print res.text
