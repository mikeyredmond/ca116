#!/usr/bin/env python

n = input()
i = 0
count = 0

while i < n:
   m = raw_input()
   if m == "one":
      count = count + 1
   elif m == "two":
      count = count + 2
   elif m == "three":
      count = count + 3
   elif m == "four":
      count = count + 4
   elif m == "five":
      count = count + 5
   i += 1
print count
