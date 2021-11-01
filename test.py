# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:49:57 2021

@author: Grant Huang
"""
from complex import Complex

'''
z1 = c.Complex(0, 1)
z2 = c.Complex(1, 1)
print("z1=" + str(z1))
print("z2=" + str(z2))
print("abs(z2)=" + str(abs(z2)))
print("z1+z2=" + str(z1 + z2))
print("z2-z1=" + str(z2 - z1))
print("z1*z2=" + str(z1*z2))
print("z2/z1=" + str(z2/z1))
'''
z3 = Complex(-1, 0)
print("z3=" + str(z3))
root = Complex.squareRoot(z3)
print("sqrt(z3)=" + str(root))

power = Complex(4,0)
product = z3**4
print("z3^3="+str(product))