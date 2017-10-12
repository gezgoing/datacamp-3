
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:15:36 2017

@author: Ivan
"""

import urllib.request
import urllib.parse
import re
import time


url = 'http://pythonprogramming.net'
values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

time.sleep(15)