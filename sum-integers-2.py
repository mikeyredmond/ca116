#!/usr/bin/env python

import sys
file = sys.argv[1]
total = 0
with open(file, "r") as f:
   file = f.readline()
   while 0 < len(file):
      total = total + int(file)
      file = f.readline()
print total
