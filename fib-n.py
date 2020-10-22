#!/usr/bin/env python

n = input()

i = 0
while i < n:
   if i == 0:
      print 0
   elif i == 1:
      print 1
      x = 1
      z = 0
   else:
      y = x + z
      z = x
      x = y
      print y
   i = i + 1
