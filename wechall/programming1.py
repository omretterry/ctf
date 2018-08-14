#!/usr/bin/env python

import urllib2
import webbrowser  
headers = {'Cookie':'WC=10545137-41483-LE03v79NlZdHHH9H'}
req = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?action=request',
    headers=headers)
f = urllib2.urlopen(req)
res = f.read()

webbrowser.open('http://www.wechall.net/challenge/training/programming1/index.php?answer=' + res, new=0, autoraise=True)  
print 'http://www.wechall.net/challenge/training/programming1/index.php?answer=' + res
req2 = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?answer=' + res,
    headers=headers)
f2 = urllib2.urlopen(req)
print f2.read()
