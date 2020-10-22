#!/usr/bin/env python

i = 0
l = []
total = 0
s = raw_input()

while s != "end":
   l.append(s)
   s = raw_input()
   i += 1

j = 0
while j < len(l):
   print j, len(l), l[j]
   j += 1
