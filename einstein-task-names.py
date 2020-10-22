#!/usr/bin/env python

s = raw_input()

while s != "end":
   i = 0

   while i < len(s) and s[i] != "/":
      i += 1

   j = i + 1
   while j < len(s) and s[j] != "/":
      j += 1

   k = j + 1
   while k < len(s) and s[k] != "/":
      k += 1

   if s[k + 1:][len(s[k + 1:]) - 1] == "y":
      print s[k + 1:]

   s = raw_input()
