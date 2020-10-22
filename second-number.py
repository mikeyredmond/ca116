#!/usr/bin/env python

s = raw_input()
j = 0

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and "0" <= s[j] and s[j] <= "9":
        j = j + 1

k = j + 1
while k < len(s) and (s[k] < "0" or "9" < s[k]):
    k = k + 1

if k < len(s):
    l = k
    while l < len(s) and "0" <= s[l] and s[l] <= "9":
        l = l + 1
    print s[k:l], k
