import math
import sys
import formulas
import helper
import main
import newton
import secant
import bisection

def test_newton(capsys):
    equa = [-1, 0, 6, -5, 1]
    prec = 12
    newton.newton(equa, prec)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stderr == ""
    assert captured_stdout == "('x =', 0.5)\n('x =', '0.522727272727')\n"\
    "('x =', '0.522740003514')\n('x =', '0.522740003526')\n"

def test_secant(capsys):
    equa = [-1, 0, 6, -5, 1]
    prec = 8
    secant.secant(equa, prec)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stderr == ""
    assert captured_stdout == "('x =', '0.00000000')\n('x =', '0.00000000')\n"

def test_helper(capsys):
    helper.helper()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stderr == ""
    assert captured_stdout == "USAGE\n    ./105torus opt a0 a1 a2 a3 a4 n\n"\
    "DESCRIPTION\n    opt       method option:\n                   "\
    "1 for the bisection method\n                   2 for Newton's method\n"\
    "                   3 for the secant method\n    a[0-4]    coefficients"\
    " of the equation\n    n         precision (the application of the"\
    " polynomial to the solution should be smaller than 10^-n)\n"