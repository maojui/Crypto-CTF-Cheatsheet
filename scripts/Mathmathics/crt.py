import operator
from functools import reduce
from Crypto.Util.number import inverse

def crt(remainders, modules):
    """
    Solving Chinese Remainder Theorem
    @modules and @remainders are lists.
    """
    x = 0
    N = reduce(operator.mul, modules)
    for i, module in enumerate(modules):
        if module == 1:
            continue
        Ni = N // module
        b = inverse(Ni, module)
        x += remainders[i] * Ni * b
    return x % N