# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:32:25 2020

@author: ghostkiller1704
"""


import sympy as sym

func = input("enter your function, e.g. x**4+3*x**2\n")
f = sym.sympify(func) #converts the given function into a readable form for sympy

sub = input("enter x \n") #substitute for x

x = sym.Symbol('x')

y = f.evalf(subs={x:sub}) #finds the y value for the given function so later y-axis intercept can be calculated
print("\n",y, "is f","(",sub,")")

ans = (sym.diff(f)) #this differentiates the function
m = ans.evalf(subs={x: sub}) #finds the slope of the tangent function
print("\n",m, "is m")

c = y - m*int(sub) #finds the y-axis intercept of the tangent function
print("\n",c, "is c")

print("\n","the tangent funtion is:","f(x)=",int(m),"x",int(c))