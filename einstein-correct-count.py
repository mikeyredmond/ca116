#!/usr/bin/env python

s = raw_input()
total = 0

while s != "end":
   if s[len(s) - 7:] == "correct" and s[len(s) - 9:] != "incorrect":
      total += 1

   s = raw_input()

print total
