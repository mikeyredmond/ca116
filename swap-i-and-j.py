#!/usr/bin/env python

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]
   i = 1
   j = 2

f = a[i]
l = a[j]

tmp = f
a[i] = l
a[j] = f
