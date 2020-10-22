#!/usr/bin/env python

import sys
total = 0
i = 1
while i < len(sys.argv):
   t = sys.argv[i]
   with open(t) as f:
      t = f.readline()
      while 0 < len(t):
         total = total + int(t)
         t = f.readline()
      i += 1
print total
