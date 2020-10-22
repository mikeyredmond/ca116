#!/usr/bin/env python

s = raw_input()
t = ""

i = 0
while i < len(s) / 2 and s[len(s) - i - 1] == s[i]:
    i = i + 1

if not(i < len(s) / 2):
    print "palindrome"
