#!/usr/bin/env python

n = 8
longest = ""

i = 0
while i < n:
   line = raw_input()
   if len(longest) < len(line):
      longest = line
   i = i + 1

print longest
