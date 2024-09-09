##
## EPITECH PROJECT, 2020
## newton.py
## File description:
## blabla
##

import math
import sys
import formulas
import helper

def newton(equa, prec):
    x = 0.5
    h = formulas.equation(equa, x) / formulas.derivation(equa, x)
    count = 0
    f = prec
    flag = f
    print("x =", x)
    while abs(h) >= math.pow(10, -f):
        h = formulas.equation(equa, x) / formulas.derivation(equa, x)
        x = x - h
        if abs(h) >= math.pow(10, -f):
            print("x =", formulas.printStr(round(x, f), flag))
            count = count + 1
            if (count > 200):
                exit(84)
        else:
            break
    return 0
