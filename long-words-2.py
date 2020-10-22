#!/usr/bin/env python

if __name__ == "__main__":
   a = ["cat", "elephant", "mouse", "lizzard", "horse", "mongoose"]

i = 0
while i < len(a) and len(a[i]) < 6:
   i += 1

if i < len(a):
   print a[i]
