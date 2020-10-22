#!/usr/bin/env python

with open("hello.txt", "w") as f_output:
   output = "Hello world." + "\n"
   f_output.write(output)
