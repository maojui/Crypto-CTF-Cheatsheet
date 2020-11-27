import random
from Crypto.Util.number import getPrime, getRandomRange, inverse, GCD

class Paillier:
    """
    ref: https://en.wikipedia.org/wiki/Paillier_cryptosystem
    
    Paillier(tup) :
        @tup : (n,g) for public key, n=p*q, g is a random integer in field n*n
             : (n,g,p,q) for private key, generate (mu, λ)
    
    """
    def __init__(self,tup):
        "Choose two large distinct primes p and q and compute N = (p**2) * q"
        if len(tup) == 2 :
            self.pubkey = tup
        elif len(tup) == 4 :
            n, g = tup[:2]
            p, q = tup[2:]
            assert n == p*q, 'Input private key raise error.'
            self.pubkey = (n,g)
            λ = (p-1)*(q-1)
            mu = inverse(self._L(pow(g,λ,n*n)),n)
            self.privkey = (n,λ,mu)
        else :
            raise ValueError('Paillier(tup) : \n\t@tup : \n\t\t(n,g) for public key \n\t\t(n,g,p,q) for private key')

    def _L(self, u) :
        return (u - 1) // self.pubkey[0]

    def encrypt(self,m):
        """
        return (g^m * r^n) % n^2
        """
        n,g = self.pubkey
        mods = n*n
        gm = pow(g,m,mods)
        r = 0
        while GCD(r,n) != 1 :
            r = random.randint(0,n-1)
        return (gm * pow(r,n,mods)) % mods
    
    def decrypt(self, c):
        n,λ,mu = self.privkey
        mes = pow(c,λ,n*n)
        mes = self._L(mes)*mu % n
        return mes
    
    @classmethod
    def generate(cls,bits):
        p = getPrime(bits//2)
        q = getPrime(bits//2+ bits%2)
        g = getRandomRange(0, (p*q)**2)
        n = p * q
        return cls((n,g,p,q))

if __name__ == "__main__":

    paillier = Paillier.generate(1024)
    m = getPrime(1000)
    c = paillier.encrypt(m)
    assert m == paillier.decrypt(c)