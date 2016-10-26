#!/usr/bin/python3

"""
Michael duPont - sumvals.py
Example file using the begin(s) library

Usage: python3 sumvals.py [-h] [other args...]

Demo example: invoke makerand | cut -f1 -d- | xargs python3 sumvals.py
"""

#library
import begin

@begin.start
#Parameter descriptions read from annotations
#begin.start can only be used with one function per file
def main(*vals: 'Values to be summed',
         setabs: 'Sums absolute values'=False):
    """Sums an arbitrary number of integer arguments
    """
    if setabs:
        vals = [abs(int(val)) for val in vals]
    else:
        vals = [int(val) for val in vals]
    print(sum(vals))
