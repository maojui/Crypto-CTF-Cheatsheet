from Crypto.Util.number import GCD, isPrime

def primegen():
    """
    Generates primes lazily via the sieve of Eratosthenes
    Input: none
    Output:
        Sequence of integers
    Examples:
    >>> list(takewhile(lambda x: x < 100, primegen()))
    [2, 3, 5, 7, 11, 13, 8, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
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
 
def pollard_rho(N, f=None):
    """
    Pollard's rho algorithm can fail for some inputs. 
    Simply change the f or seed values if it fails.
    """
    x, y, d = 2, 2, 1
    if f == None :
        f = lambda x: (x*x+1) % N
    tmp = []
    while d <= 1:
        x = f(x)
        if not x in tmp :
            tmp.append(x)
        else:
            break
        y = f(f(y))
        d = GCD(x - y, N)
        if d != 1 : 
            if 1 < d < N : return d
            if d == N : return None
    return d

def pollard_pm1(N):
    """    
    For one of N's prime p, 
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all (p-1)'s factor were iterated by b
    Then it can be factorization by pollard_pm1.

    ** It may failed if the degree of (p-1)'s factors is greater than 1. **
    """
    if isPrime(N):
        return N
    a = 2
    primes = primegen()
    for b in primes :
        try :
            a = pow(a, b, N)
            p = GCD(a - 1, N)
            if 1 < p < N:
                return p
        except :
            print("Pollard P-1 Failed.")
            return 0

def pollard_brute(N):
    """    
    For one of N's prime p, 
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all (p-1)'s factor were iterated by b
    Then it can be factorization by pollard_pm1.
    """
    a = 2
    b = 1
    factors = []
    if isPrime(N) : return N
    try :
        while True:
            a = pow(a, b, N)
            p = GCD(a - 1, N)
            if 1 < p < N:
                factors.append(p)
                print(f"factor found: {p}")
                q = N // p 
                if isPrime(q) :
                    print(f"factor found: {q}")
                    factors.append(q)
                    return factors
            b += 1
    except:
        return factors


if __name__ == "__main__":

    import random
    from functools import reduce
    from operator import mul
    ps = primegen()
    small_primes = [next(ps) for _ in range(1000)]
    while True :
        ps = [random.choice(small_primes) for i in range(30)]
        p = reduce(mul, ps) + 1
        if isPrime(p) :
            break
    while True :
        qs = [random.choice(small_primes) for i in range(30)]
        q = reduce(mul,qs) + 1
        if isPrime(q) :
            break
    n = p*q


    print(f"p = {p}")
    print(f"q = {q}")
    print(pollard_brute(p*q))
    print(pollard_pm1(p*q))
    print(pollard_rho(455459))