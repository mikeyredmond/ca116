#!/usr/bin/env python

if __name__ == "__main__":
   a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

i = 0
s = a[i]
p = 0

i += 1
while i < len(a):
   if a[i] < s:
      s = a[i]
      p = i
   i += 1

print p
