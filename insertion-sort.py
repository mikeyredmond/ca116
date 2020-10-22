#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
   a.append(int(s))
   s = raw_input()

i = 0
while i < len(a):
   v = a[i]
   p = i
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v
   i += 1

j = 0
while j < len(a):
   print a[j]
   j += 1
