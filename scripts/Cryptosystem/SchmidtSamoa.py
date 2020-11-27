from Crypto.Util.number import GCD, inverse, getPrime

lcm = lambda a, b: a * b // GCD(a, b)

class SchmidtSamoa:
    """
    ref:  https://en.wikipedia.org/wiki/Schmidt-Samoa_cryptosystem
    
    SchmidtSamoa(tup) :
        @tup : (n,) for public key, n=p*p*q
             : (n,p,q) for private key, generate (d,module)
    
    """
    def __init__(self,tup):
        "Choose two large distinct primes p and q and compute N = (p**2) * q"
        if len(tup) == 1 :
            self.pubkey = tup[0]
            self.privkey = None
        elif len(tup) == 3 :
            n, p, q = tup
            assert n == pow(p,2)*q, 'Input private key raise error.'
            self.pubkey = n
            self.privkey = (inverse(self.pubkey, lcm(p-1,q-1)), p*q)
        else :
            raise ValueError('SchmidtSamoa(tup) : \n\t@tup : \n\t\t(n) for public key \n\t\t(n,p,q) for private key')

    def encrypt(self,m):
        "c = m**N % N  ( N = p**2 * q)"
        return pow(m,self.pubkey,self.pubkey)
        
    def decrypt(self,c):
        """
        m = c**d % pq
        """
        if self.privkey :
            d , module = self.privkey
            return pow(c,d,module)
        else :
            raise ValueError('Could not decrypt without privkey.')
    
    @classmethod
    def generate(cls,bits):
        p = getPrime(bits//3)
        q = getPrime(bits//3+ bits%3)
        n = p * p * q
        return cls((n,p,q))

if __name__ == "__main__":
    schmidtSamoa = SchmidtSamoa.generate(1024)
    m = getPrime(500)
    c = schmidtSamoa.encrypt(m)
    assert m == schmidtSamoa.decrypt(c)