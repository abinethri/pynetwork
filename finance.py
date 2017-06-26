# Note - this code must run in Python 2.7.6 and you must download
# BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

serviceurl = 'https://www.google.com/finance?'

address = raw_input('Enter stock symbol: ')
url = serviceurl + urllib.urlencode({'q':address})
print 'Retrieving', url
uh = urllib.urlopen(url)
html = uh.read() 
print 'Retrieved',len(html),'characters'
#print html 

soup = BeautifulSoup(html)
tags = soup('span')

for tag in tags:
    #print "Span: ", tag 
        price = tags[9].text 

print "Pos", price      
print "--"  
  


