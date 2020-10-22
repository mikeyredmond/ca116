#!/usr/bin/env python

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

total = 0
i = 0
while i < len(a):
   if a[i] != "":
      total += 1
   i += 1

print total
