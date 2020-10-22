#!/usr/bin/env python

s = raw_input()
a = []
i = 0
while s != "end":
   a.append(int(s))
   s = raw_input()

n = input()
while i < len(a) and a[i] <= n:
   i = i + 1

print i
