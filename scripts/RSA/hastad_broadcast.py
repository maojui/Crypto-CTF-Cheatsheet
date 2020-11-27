import operator
from gmpy2 import iroot
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

def hastad_broadcast(cipher, module, exponent):
    """    
    Chinese Remainder
    If the same message, encrypt by same exponent but different module
    hastad broadcast attack may solved it.
    
        usage  : hastad_broadcast([C1,C2,C3],[N1,N2,N3])
        return : C = M^e mod (N1*N2*N3)
    
    if M^e < N1*N2*N3 : solved.
    """
    assert len(cipher) == len(module), "Amount of (cipher, modulo) pair unmatch."
    C = crt(cipher,module)
    m, root = iroot(C, exponent)
    if root == True :
        return int(m)