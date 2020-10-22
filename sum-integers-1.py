#!/usr/bin/env python

import sys

num = sys.stdin.readlines()
total = 0
i = 0
while i < len(num):
   total = total + int(num[i])
   i += 1

total = str(total)
sys.stdout.write(total + "\n")
