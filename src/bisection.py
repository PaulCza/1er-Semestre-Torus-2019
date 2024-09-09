##
## EPITECH PROJECT, 2020
## bisection.py
## File description:
## blabla
##
import math
import sys
import formulas
import helper
def bisection(equa, prec):
    a = 0
    b = 1
    flag = 1
    f = prec
    if (formulas.equation(equa, a) * formulas.equation(equa, b) >= 0): 
        exit(84)

    c = a 
    while ((b-a) >= math.pow(10, -f)): 
        c = (a+b)/2
        if (formulas.equation(equa, c) == 0.0): 
            break
        if (formulas.equation(equa, c)*formulas.equation(equa, a) < 0): 
            b = c 
        else: 
            a = c
        c = round(c, f)
        print("x =", formulas.printStr(c, flag))
        if (flag != f):
            flag = flag + 1
    return 0