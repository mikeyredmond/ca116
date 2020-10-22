#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
   a.append(s)
   s = raw_input()

r = raw_input()
b = ""
while r != "end":
   if r.isdigit():
      if b:
         b += " "
      b += a[int(r)]
   else:
      print b
      b = ""
   r = raw_input()

if b:
   print b
