from Crypto.Util.number import GCD, isPrime, get_primes

def get_primes(n):
    """ 
    High speed to generate all primes which is smaller than n.
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 
    """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * int((n//3))
    for i in range(1,int(n**0.5/3)+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * int((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * int((n//6-k*(k-2*(i&1)+4)//6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(1,int(n/3-correction)) if sieve[i]]

def pollard_rho(N):
    """    
    For one of N's prime p, 
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all factor are appear in b
    Then it can be solved by Pollard_P-1.
    """
    factor, cycle = 1,1    
    x, fixed = 2,2
    while factor == 1:
        print('Pollard rho cycle : {}'.format(cycle))
        count = 1
        cycle *= 2
        while count <= cycle and factor <= 1:
            x = (x*x + 1) % N
            factor = GCD(x - fixed, N)
            count += 1
        fixed = x
    return factor

def pollard_pm1(N,prange=10000000):
    """    
    For one of N's prime p, 
        1. If (p-1) is a K-smooth number. (k is small)
        2. When all factor are appear in b
    Then it can be solved by Pollard_P-1.
    """
    if isPrime(N):
        return N
    test_p = iter(get_primes(prange))
    a = 2
    while True:
        try :
            b = next(test_p)
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
        2. When all factor are appear in b
    Then it can be solved by Pollard_P-1.
    """
    a = 2
    b = 1
    while True:
        if b % 10000 == 0:
            print('pollard brute : ',b)
        a = pow(a, b, N)
        p = GCD(a - 1, N)
        if 1 < p < N:
            return p
        b += 1
