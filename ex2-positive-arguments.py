#!/usr/bin/env python

import sys

n = sys.argv[1:]

i = 0
while i < len(n):
   if 0 < int(n[i]):
      print int(n[i])
   i += 1
