#!/usr/bin/env python

german = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

a = []
import sys
words = sys.stdin.read().split()

i = 0
while i < len(words):
   word = words[i]
   if word in german:
      print german[word]
   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1
