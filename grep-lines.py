#!/usr/bin/env python

import sys
args = sys.argv[1:]

k = args[0]
p = []
match = []

s = raw_input()

while s != "end":
   p.append(s)
   s = raw_input()

i = 0

while i < len(p):
   j = 0

   string = p[i]
   while j < len(string) and not (k in string):
      j += 1

   if j < len(string):
      match.append(string)

   i += 1

a = 0

while a < len(match):
   print match[a]
   a += 1
