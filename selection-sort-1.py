#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
   a.append(int(s))
   s = raw_input()

i = 0
j = 1
while j < len(a):
   if a[j] < a[i]:
      i = j
   j = j + 1

print i
