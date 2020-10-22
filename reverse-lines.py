#!/usr/bin/env python

i = 0
k = []
s = raw_input()

while s != "end":
   k.append(s)
   s = raw_input()
   i += 1

j = len(k) - 1

while 0 <= j:
   print k[j]
   j = j - 1
