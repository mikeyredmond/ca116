#!/usr/bin/env python

n = input()
m = 5

i = 0
while i < m:
   c = input()
   if c > n:
      print "higher"
   elif c == n:
      print "equal"
   else:
      print "lower"
   n = c
   i = i + 1
