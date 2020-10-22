#!/usr/bin/env python

n = raw_input()

m = raw_input()

t = raw_input()

if len(m) < len(n) and len(t) < len(n):
  print n
elif len(n) < len(m) and len(t) < len(m):
  print m
else:
  print t
