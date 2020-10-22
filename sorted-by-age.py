#!/usr/bin/env python

import sys

def main():
   d = {}
   a = []
   s = sys.stdin.readline()
   while 0 < len(s):
      t = s.strip().split(' ', 1)
      if len(t) > 1:
         a.append(t[0])
         d[t[0]] = t[1]
      s = sys.stdin.readline()
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j][6:] < a[p][6:]:
            p = j
         elif a[j][6:] == a[p][6:] and a[j][3:5] < a[p][3:5]:
            p = j
         elif a[j][6:] == a[p][6:] and a[j][3:5] == a[p][3:5]:
            if a[j][:2] < a[p][:2]:
               p = j
         j += 1

      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i += 1
   lastloop = 0
   while lastloop < len(a):
      print d[a[lastloop]]
      lastloop += 1

if __name__ == '__main__':
   main()
