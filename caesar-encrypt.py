#!/usr/bin/env python

import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alp = lower + upper
cip = lower[n:] + lower[:n] + upper[n:] + upper[:n]
dic = {}

i = 0
while i < len(alp):
   dic[alp[i]] = cip[i]
   i += 1

s = sys.stdin.read()
g = ""
i = 0
while i < len(s):
   if s[i] in dic:
      g = g + dic[s[i]]
   else:
      g = g + s[i]
   i += 1

sys.stdout.write(g)
