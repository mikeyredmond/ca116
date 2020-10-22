#!/usr/bin/env python

s = raw_input()
i = 0
end = 0
start = 0
while i < len(s):
   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1
   if start < len(s):
      print s[start:end]
   start = end + 1
   i = i + 1
