#sqrt(x) trough stirling factorial approximation

#consts 
rs2pi = 0.39894228040143267794 # reciprocal of sqrt(2pi)
e = 2.71828182845904523536 # euler's


def sqrt(x : float, m : int = 10) -> float:
    iters = int(x*m*m)
    eoi = e/iters ; prod = 1
    for n in range(1, iters+1):
        prod *= n*eoi
    prod *= rs2pi / m
    return(prod)
