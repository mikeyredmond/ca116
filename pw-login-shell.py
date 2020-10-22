#!/usr/bin/env python

s = raw_input()
j = ""
k = ""

while s != "end":
   i = 0
   while i < len(s) and s[i] != ":":
      i += 1
   if i < len(s):
      j = s[:i]
   l = len(s) - 1
   while l < len(s) and s[l] != ":":
      l = l - 1
   if l < len(s):
      k = s[l + 1:]
      print j, k
   s = raw_input()
