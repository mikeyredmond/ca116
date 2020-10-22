#!/usr/bin/env python

import sys
line = sys.stdin.readline()
a = []
i = 0
while i < len(line):
   a = line.split("/")
   a = a[len(a) - 1].split()
   print a[0]
   line = sys.stdin.readline()
   i += 1
