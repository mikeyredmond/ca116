#!/usr/bin/env python

import sys
t = sys.stdin.readline().strip()
h = {}
while len(t) != 0:
   h[".".join(t.split(".")[0:2])] = t.split(".")[2]
   t = sys.stdin.readline().strip()
for file in h:
   if h[file] == "correct":
      print file
