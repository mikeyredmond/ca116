#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
   if not (s in a):
      a.append(s)
   s = raw_input()
j = 0
while j < len(a):
   print a[j]
   j += 1
