#!/usr/bin/python
import  sys, urllib
from BeautifulSoup import BeautifulSoup as BS

args = sys.argv
sock = urllib.urlopen("http://codeforces.com/contest/" + args[-2] + "/problem/" + args[-1])
soup = BS(sock)
_in = soup.findAll('div', {'class': 'input'})
_out = soup.findAll('div', {'class':'output'})

cnt = 0
for i in _in:
  ins = i.pre.contents
  f = open(args[-2] + args[-1] + str(cnt) + ".in", 'w')
  for line in ins:
    try:
      f.write(line.replace('<br />', '') + '\n')
    except TypeError, e:
      None
  cnt = cnt + 1
  f.close()
  
cnt = 0
for o in _out:
  outs = o.pre.contents
  f = open(args[-2] + args[-1] + str(cnt) + ".out", 'w')
  for line in outs:
    try:
      f.write(line.replace('<br />', '') + '\n')
    except TypeError, e:
      None
  cnt = cnt + 1
  f.close()
