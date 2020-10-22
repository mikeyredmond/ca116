#!/usr/bin/env python

def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   while i < len(a) / 2:
      swap(a, i, len(a) - i - 1)
      i += 1

a = [4, 3, 1, 2]

def main():
   swap(a, 2, 3)
   print a

   reverse(a)
   print a

if __name__ == "__main__":
   main()
