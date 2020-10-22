#!/usr/bin/env python

total = 0
s = raw_input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1

   if s[i + 1:i + 3] == "WI":
      total = total + 1

   s = raw_input()

print total
