#!/usr/bin/env python

t = 0

while t != 1000:
   s = raw_input()
   j = 0
   while j < len(s) and (s[j] != "+"):
      j += 1

   a = s[:j]
   b = s[j + 1:]
   t = int(a) + int(b)
   print t
