#!/usr/bin/env python

n = input()

if 2 < n < 20 and n % 2 == 1 and n % 3 != 0:
   print "prime"
elif n == 2 or n == 3:
   print "prime"
else:
   print "not prime"
