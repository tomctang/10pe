## Pre-running functions

# C2 Year 12

import numpy as np
import random
import time
g=9.8
e=np.e
import sympy as sym
import sympy.abc as abc

# Change function ncr's name
def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        raise ValueError
    else:
        return n*fact(n-1)
# choose r out of n (returns possibilities)
def ncr(n, r):
    return fact(n)/(fact(r)*fact(n-r))

def pvalue(n:int, r:int, p:float):
    pval=0
    for i in range(r+1):
        pval+=ncr(n,i)*p**i*(1-p)**(n-i)
    return pval

# Only for x<= something
def critical_left(n:int, r:int, p:float, sig:float):
    pval=pvalue(n, r, p)
    print(pval)
    # returns true if accept H0 otherwise returns false
    return pval>sig/100

# Only for x>=something
def critical_right(n:int, r:int, p:float, sig:float):
    pval=1-pvalue(n, r-1, p)
    print(pval)
    return pval>sig/100

# C1 Year 13

def inverse(f):
    inverse=sym.solve(f - abc.y, abc.x)
    sym.pprint(inverse)
    
def arithseqsum(first_number:float, last_number:float, numbers:int):
    return numbers/2*(first_number+last_number)

def geoseqsum(start_number, end_number, common_ratio):
    return (common_ratio*end_number-start_number)/(common_ratio-1)

def sigma(func, r, end):
    return sum(func(x) for x in range(r, end + 1))

def trapezium(intervals, start_x, end_x, func):
    if intervals<=0:
        raise ZeroDivisionError('intervals has to be positive')
    int_len=(end_x-start_x)/intervals
    xvals=[start_x,end_x]
    for n in range(1,intervals):
        i=int_len*n+start_x
        xvals.append(i)
    for i in range(len(xvals)):
        xvals[i]=func(xvals[i])
    for i in range(2,len(xvals)):
        xvals[i]*=2
    return int_len/2*sum(xvals)

def lower_bound(intervals,start_x,end_x,func):
    if intervals<=0:
        raise ZeroDivisionError('intervals has to be positive')
    int_len=(end_x-start_x)/intervals
    n=list(range(intervals))
    print(n)
    for i in range(len(n)):
        n[i]*=int_len
    num_sum=0
    for j in range(len(n)):
        num_sum+=func(j)
    return num_sum

def upper_bound(intervals,start_x,end_x,func):
    if intervals<=0:
        raise ZeroDivisionError('intervals has to be positive')
    int_len=(end_x-start_x)/intervals
    n=list(range(1,intervals+1))
    for i in range(len(n)):
        n[i]*=int_len
    num_sum=0
    for j in range(len(n)):
        num_sum+=func(j)
    return num_sum

def fixed_point(iterations,func,starting_value):
    val=starting_value
    for _ in range(iterations):
        val=func(val)
    return val

sq = lambda x: (-1)**(x+1)/(2*x-1)
aa = sigma(sq, 1, 10000)
# print(4*aa)  # 级数和 收敛到pi

# C2 Year 13

def projtime(velocity, angle):
    #  Assumes there are no wind and air resistance
    y=velocity*np.sin(np.radians(angle))
    return y*2/g

def projrange(velocity, angle):
    x=velocity*np.cos(np.radians(angle))
    y=velocity*np.sin(np.radians(angle))
    t=y*2/g
    return x*t

def upwards_friction(m, mu, angle):
    w=m*g
    n=w*np.cos(np.radians(angle))
    ff=mu*n
    fgp=w*np.sin(np.radians(angle))
    return ff+fgp

def downwards_friction(m, mu, angle):
    w=m*g
    n=w*np.cos(np.radians(angle))
    ff=mu*n
    fgp=w*np.sin(np.radians(angle))
    return fgp-ff

def pythagorean(a,b):
    return np.sqrt(a**2+b**2)

def pythagorean3(a,b,c):
    return np.sqrt(a**2+b**2+c**2)