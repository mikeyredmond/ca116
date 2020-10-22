#!/usr/bin/env python

a = input()

b = input()

c = input()

if b + c <= a or a + c <= b or a + b <= c:
   print "no"
elif a < b + c and b < a + c and c < a + b:
   print "yes"
