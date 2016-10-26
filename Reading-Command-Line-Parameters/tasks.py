#!/usr/bin/python3

"""
Michael duPont - tasks.py
Example task file for the invoke library

Usage: invoke [-h] (func_name) [other args...]

Demo Example: invoke makerand -s ',' | xargs invoke sumvals
Note: Because of arg parsing, this fails if the first int is negative
"""

# pylint: disable=W0613

#stdlib
from random import sample
#library
from invoke import task

#Parameter descriptions given in decorator call
@task(help={
    'num': 'Number of random ints',
    'minval': 'Minimum possible value',
    'maxval': 'Maximum possible value',
    'sep': 'Separator in printed string'
})
#Context (ctx) must be the first parameter if function definition
#Annotations and var expanders (*argv) can't be used
def makerand(ctx, num=10, minval=-20, maxval=20, sep=' '):
    """Prints a string of random ints"""
    print(sep.join([str(v) for v in sample(range(minval, maxval+1), num)]))

@task(help={
    'vals': 'Values to be summed',
    'setabs': 'Sums absolute values'
})
def sumvals(ctx, vals, setabs=False):
    """Sums a ','-separated string of ints"""
    if setabs:
        vals = [abs(int(val)) for val in vals.split(',')]
    else:
        vals = [int(val) for val in vals.split(',')]
    print(sum(vals))
