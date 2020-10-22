#!/usr/bin/env python

n = raw_input()
a = []

while n != "end":
   a.append(int(n))
   n = raw_input()


i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i = i + 1

m = 0
while m < len(a):
   print a[m]
   m = m + 1
