#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## formulas.py
## File description:
## a
##


def equation(equa, x):
    a = equa[0]
    b = equa[1]
    c = equa[2]
    d = equa[3]
    e = equa[4]
    return e*(x*x*x*x) + d*(x*x*x) + c*(x*x) + b*(x) + a

def derivation(equa, x):
    b = equa[1]
    c = equa[2]
    d = equa[3]
    e = equa[4]
    f = b
    g = 4 * e * (x * x * x) 
    h = 3 * d * (x * x)
    i = 2 * c * x 
    result = g + h + i + f
    if result == 0:
        exit(84)
    
    return result

def printStr(FloatNumber, Precision):
    return "%0.*f" % (Precision, FloatNumber)
