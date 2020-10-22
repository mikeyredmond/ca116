#!/usr/bin/env python

total = 0

i = 0
while i <= 4:
   n = input()
   if n < 0:
      n = (n * - 1)
   i = i + 1
   total = total + n

print total
