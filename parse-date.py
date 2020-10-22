#!/usr/bin/env python

s = raw_input()
j = 0

i = 0
while i < len(s) and ("A" <= s[i] and s[i] <= "z"):
   i = i + 1

while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and "0" <= s[j] and s[j] <= "9":
      j = j + 1

k = j
while k < len(s) and ("A" <= s[k] and s[k] <= "z"):
   k = k + 1

l = k + 1
while l < len(s) and ("A" <= s[l] and s[l] <= "z"):
   l = l + 1

m = l
while m < len(s) and (s[m] < "0" or "9" < s[m]):
   m = m + 1

if m < len(s):
   while m < len(s) and "0" <= s[m] and s[m] <= "9":
      m = m + 1

print s[k + 1:l], s[i:j] + s[j:k] + ",", s[l + 2:m], "(" + s[0:i - 1] + ")"
