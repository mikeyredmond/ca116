#!/usr/bin/env python

n = raw_input()
a = []

while n != "end":
   a.append(int(n))
   n = raw_input()


j = 0
i = input()
while i < len(a):
   if a[i] < a[j]:
      j = i
   i = i + 1

print j
