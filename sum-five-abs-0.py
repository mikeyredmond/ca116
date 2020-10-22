#!/usr/bin/env python

total = 0

n = input()
while n != 0:
   if 0 < n:
      total = total + n
   else:
      total = total - n
   n = input()
print total
