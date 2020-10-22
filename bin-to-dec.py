#!/usr/bin/env python

n = raw_input()
s = 0

i = 0
while i < len(n):
   s += ((2 ** (len(n) - i)) * int(n[i])) / 2
   i += 1


print s
