#!/usr/bin/env python

if __name__ == "__main__":
   a = [1, 5, 6, 6, 10, 12]
   p = 4
   v = 8

a.append(v)
i = len(a) - 1

while i >= p:
   if i == p:
      a[i] = v
   else:
      tmp = a[i]
      a[i] = a[i - 1]
      tmp = a[i - 1]

   i -= 1
