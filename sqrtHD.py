from math import factorial

def sqrt(N):
    H = 9
    h = 1/2**(2*H)
    def f(x): return(x**N)
    s = 0
    ak = 1
    acc = 10**(-15)
    for k in range(0, int(1/h)):
        rs = (-1)**k * ak * f(1-k*h)
        if abs(rs) < acc: break
        s += rs
        ak *= (1/2 - k)/(k+1)
    HD = s*2**H
    return(HD)
