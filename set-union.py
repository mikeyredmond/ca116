#!/usr/bin/env python

import sys
with open("a.txt", "r") as t:
   a = t.read().split()

h = {}
i = 0
while i < len(a):
   words_a = a[i]
   if words_a not in h:
      h[words_a] = True
   i += 1

with open("b.txt", "r") as t:
   b = t.read().split()

p = 0
while p < len(b):
   words_b = b[p]
   if words_b not in h:
      h[words_b] = True
   p += 1

for words in h:
   print words
