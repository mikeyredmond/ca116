#!/usr/bin/env python

n = input()
a = 0
b = 1

i = 0
while i < n:
   if a < n:
      print a
      c = b
      b = b + a
      a = c
   i = i + 1
