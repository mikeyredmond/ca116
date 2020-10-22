#!/usr/bin/env python

import sys
with open(sys.argv[1], "w") as f_output:
   output = "Hello world." + "\n"
   f_output.write(output)
