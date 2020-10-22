#!/usr/bin/env python

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"
s = raw_input()

while s != "end":
   t = ""
   l = 0
   while l < len(s):
      pos = -1
      i = 0
      while i < len(upper):
         if s[l] == upper[i]:
            pos = i
         i += 1

      if pos == -1:
         t = t + s[l]
      else:
         t = t + lower[pos]
      l += 1

   print t
   s = raw_input()
