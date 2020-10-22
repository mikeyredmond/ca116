#!/usr/bin/env python

pi = 3.141

def circumference(r):
   return r * pi * 2

def area(r):
   return pi * r * r

def main():
   print circumference(2)
   print area(3)

if __name__ == "__main__":
   main()
