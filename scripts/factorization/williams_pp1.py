from math import gcd, isqrt, log
from Crypto.Util.number import isPrime


def primegen():
    # From primefac
    """
    Generates primes lazily via the sieve of Eratosthenes
    Input: none
    Output:
        Sequence of integers
    Examples:
    >>> list(takewhile(lambda x: x < 100, primegen()))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    yield 2; yield 3; yield 5; yield 7; yield 11; yield 13
    ps = primegen() # yay recursion
    p = next(ps) and next(ps)
    q, sieve, n = p**2, {}, 13
    while True:
        if n not in sieve:
            if n < q: yield n
            else:
                _next, step = q + 2*p, 2*p
                while _next in sieve: _next += step
                sieve[_next] = step
                p = next(ps)
                q = p**2
        else:
            step = sieve.pop(n)
            _next = n + step
            while _next in sieve: _next += step
            sieve[_next] = step
        n += 2
 
def williams_pp1(n):
    """
    Williams' p+1 integer factoring algorithm
    Input:
        n -- integer to factor
    Output:
        Integer.  A nontrivial factor of n.
    Example:
    >>> williams_pp1(315951348188966255352482641444979927)
    12403590655726899403
    """
    factors = []
    counter = 0
    if isPrime(n) : return n
    while True:
        v = counter
        for p in primegen():
            e = int(log(isqrt(n), p))
            if e == 0: break
            for _ in range(e): 
                # Multiplies along a Lucas sequence modulo n
                v1, v2 = v, (v**2 - 2) % n
                for bit in bin(p)[3:]: 
                    if bit == "0" :
                        v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n)  
                    else :
                        v1, v2 = ((v1*v2 - v) % n, (v2**2 - 2) % n)
                v = v1
            g = gcd(v - 2, n)
            if 1 < g < n: 
                if gcd(n, g) != 1 :
                    n = n//g
                    print(f'factor found :{g}')
                    factors.append(g)
                    if isPrime(n) :
                        factors.append(n)
                        return factors
                    if n == 1: return factors
            if g == n: break
        counter += 1
        v = counter


if __name__ == "__main__":
    import random
    from functools import reduce
    from operator import mul
    ps = primegen()
    small_primes = [next(ps) for _ in range(1000)]
    while True :
        p = reduce(mul,[random.choice(small_primes) for i in range(50)]) - 1
        if isPrime(p) :
            break
    while True :
        q = reduce(mul,[random.choice(small_primes) for i in range(50)]) - 1
        if isPrime(q) :
            break
    n = p*q
    print(f"p = {p}")
    print(f"q = {q}")
    print(williams_pp1(p*q))