#!/usr/bin/env python

r = 10
a = [0] * r
s = raw_input()
while s != "end":
   a[int(s)] = a[int(s)] + 1
   s = raw_input()

i = 0
while i < len(a):
   print i, ("*" * a[i])
   i += 1
