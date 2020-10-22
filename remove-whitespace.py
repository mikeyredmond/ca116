#!/usr/bin/env python

s = raw_input()
t = " "
total = ""

i = 0
while i < len(s):
   if s[i] != t:
      total = total + s[i]
   i = i + 1

print total
