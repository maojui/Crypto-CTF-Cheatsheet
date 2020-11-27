def primegen():
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
    p = ps.next() and ps.next()
    q, sieve, n = p**2, {}, 13
    while True:
        if n not in sieve:
            if n < q: yield n
            else:
                next, step = q + 2*p, 2*p
                while next in sieve: next += step
                sieve[next] = step
                p = ps.next()
                q = p**2
        else:
            step = sieve.pop(n)
            next = n + step
            while next in sieve: next += step
            sieve[next] = step
        n += 2
 
def mlucas(v, a, n):
    """ Helper function for williams_pp1().  Multiplies along a Lucas sequence modulo n. """
    v1, v2 = v, (v**2 - 2) % n
    for bit in bin(a)[3:]: v1, v2 = ((v1**2 - 2) % n, (v1*v2 - v) % n) if bit == "0" else ((v1*v2 - v) % n, (v2**2 - 2) % n)
    return v1
 
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
    for v in count(1):
        for p in primegen():
            e = ilog(sqrt(n), p)
            if e == 0: break
            for _ in range(e): v = mlucas(v, p, n)
            g = gcd(v - 2, n)
            if 1 < g < n: return g
            if g == n: break

print(williams_pp1(315951348188966255352482641444979927))