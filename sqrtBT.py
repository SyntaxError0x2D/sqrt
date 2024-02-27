#sqrt(x) trough binomial expansion.
sumLim = 150

def ssqrt(x : float):
    s = 1 ; fact = 1 ; p = 1
    for n in range(1, sumLim+1):
        fact *= n
        p *= 0.5-(n-1)
        s += (p/fact) * (x-1)**n
    return(s)

def asqrt(x : float):
    leng = int(x+1).bit_length()
    n = 1 << (leng>>1)
    if leng & 1 == 1:
        n = (n<<1)+n
        n >>= 1
    return(n, n**2)

def sqrt(x : float):
    n, m = asqrt(x)
    return(n * ssqrt(x/m))
    
print(sqrt(1.23456789)**2)
