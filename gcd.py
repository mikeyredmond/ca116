#!/usr/bin/env python

a = input()
b = input()
while b != 0:
    gcd = b
    b = a % b
    a = gcd

print gcd
