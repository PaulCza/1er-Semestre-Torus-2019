##
## EPITECH PROJECT, 2020
## secant.py
## File description:
## blabla
##

import math
import sys
import formulas
import helper

def secant(equa, prec):
    x1 = 0
    x2 = 1
    n = 0
    xm = 0
    x0 = 0
    c = 0 
    f = prec
    if (formulas.equation(equa , x1) * formulas.equation(equa, x2) < 0): 
        while True:      
            x0 = ((x1 * formulas.equation(equa, x2) - x2 * formulas.equation(equa, x1)) / 
                            (formulas.equation(equa, x2) - formulas.equation(equa, x1)))    
            c = formulas.equation(equa, x1) * formulas.equation(equa, x0)
            x1 = x2 
            x2 = x0  
            n += 1  
            if (c == 0):  
                break  
            xm = ((x1 * formulas.equation(equa, x2) - x2 * formulas.equation(equa, x1)) / 
                            (formulas.equation(equa, x2) - formulas.equation(equa, x1))) 

            i = x0
            if x0 == 0.5:
                print("x = 0.5")
            else:
                d = str(i)
                e = f + 2
                d = d[:e]
                print("x =", formulas.printStr(round(i, f), f))
            if(abs(xm - x0) < math.pow(10, -f)):
                print("x =", formulas.printStr(round(i, f), f))
                return 0
    else: 
        print("No root")
        exit(84)