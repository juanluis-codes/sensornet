from sympy.ntheory import legendre_symbol
from sympy import *

def calculateLegendre(a, p):
    return legendre_symbol(a,p)
