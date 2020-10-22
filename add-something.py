#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
   a.append(int(s))
   s = raw_input()

n = input()
i = 0
while i < len(a):
   a[i] = a[i] + n
   print a[i]
   i = i + 1
