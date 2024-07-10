# sqrt(x) trough an area approximation of a circle

from random import random

def sqrtR(A, iters = 10000):
    A *= 0.78539816339744830962
    p = []
    for _ in range(iters): 
        x, y = random(), random()
        p.append((x, y, x**2+y**2))
    p = sorted(p, key = lambda i: i[2])
    p= p[:int(A*iters)+1]
    my, mx = max([i[0] for i in p]), max([i[1] for i in p])
    ans = (mx+my)/2
    if ans == 0: ans = 0.000001
    return(ans)

def sqrt(x : float, iters = 10000) -> float:
    if x < 0: return(False)
    if x == 0: return(0)

    if x > 1: return(1/sqrtR(1/x, iters))
    return(sqrtR(x, iters))
