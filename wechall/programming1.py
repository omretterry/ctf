#!/bin/env python

import requests

cookie = dict(WC='10544425-41483-NoNoGwa1dTXATn0R')
res = requests.get('http://www.wechall.net/challenge/training/programming1/index.php?action=request',
    cookies=cookie)

print res