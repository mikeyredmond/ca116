#!/usr/bin/env python

import sys
with open(sys.argv[1], "w") as f_output:
   i = 2
   while i < len(sys.argv):
      output = sys.argv[i] + "\n"
      f_output.write(output)
      i += 1
