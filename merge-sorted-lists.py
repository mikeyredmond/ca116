#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
   a.append(int(s))
   s = raw_input()

b = []
s = raw_input()
while s != "end":
   b.append(int(s))
   s = raw_input()

c = a + b
i = 0
while i < len(c):
   p = i
   j = i + 1
   while j < len(c):
      if c[j] < c[p]:
         p = j
      j += 1
   tmp = c[p]
   c[p] = c[i]
   c[i] = tmp
   i += 1
i = 0
while i < len(c):
   print c[i]
   i += 1
