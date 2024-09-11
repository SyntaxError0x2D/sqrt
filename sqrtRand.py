# square root trough P(max(x, y)<=R) = P(sqrt(x)<= R)

from random import random

iters = 10000

def sqrtComp(r):
    hl = []
    for _ in range(iters):
        x = random()
        y = random()
        hl.append(max(x,y))
    hl.sort()
    return(hl[int(r*iters)])

def sqrt(r):
    if r < 0: return(False)
    if r == 0: return(0)
    if r < 1: return(sqrtComp)
    if r == 1: return(1)
    if r > 1: return(1/sqrtComp(1/r))
