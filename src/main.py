#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## main.py
## File description:
## blabla
##

import math
import sys
import formulas
import helper
import bisection
import newton
import secant

def checker():
    a = len(sys.argv)
    b = 1
    while (b < a):
        try:
            val = int(sys.argv[b])
        except ValueError:
            sys.exit(84)
        b = b + 1

def main(argv):
    if (len(sys.argv) != 8):
        helper.helper()
        sys.exit(84)
    checker()
 
    flag = int(sys.argv[1])
    a0 = int(sys.argv[2])
    a1 = int(sys.argv[3])
    a2 = int(sys.argv[4])
    a3 = int(sys.argv[5])
    a4 = int(sys.argv[6])
    prec = int(sys.argv[7])
    equa = [a0, a1, a2, a3, a4]
    if (flag == 1):
        bisection.bisection(equa, prec)
    elif (flag == 2):
        newton.newton(equa, prec)
    elif (flag == 3):
        secant.secant(equa, prec)
    exit(0)
