# sqrt(x) trough a weighted fibonacci sequence

def sqrtF(n, t = 100):
    c = (n-1)/4
    
    x = 1 ; y = 1
    r = 0

    for _ in range(t):
        r = x+c*y
        y, x = x, r

    I = x/y
    return(2*I-1)

def sqrt(n, t = 100):
    if n < 0: return(False)
    if n == 0: return(0)
    return(sqrtF(n, t = 100))
