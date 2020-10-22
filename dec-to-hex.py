#!/usr/bin/env python

n = input()
hx = "0123456789abcdef"
out = ""

while n != 0:
   rem = n % 16
   div = n / 16
   out = hx[rem] + out
   n = div

print out
