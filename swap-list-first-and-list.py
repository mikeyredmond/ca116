#!/usr/bin/env python

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]

f = a[0]
l = a[len(a) - 1]

tmp = f
a[0] = l
a[len(a) - 1] = f
