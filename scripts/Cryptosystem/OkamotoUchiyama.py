from Crypto.Util.number import getRandomRange, getPrime, inverse

class OkamotoUchiyama :
    """
    ref: https://en.wikipedia.org/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem

    OkamotoUchiyama(tup) :
        @tup : (n,g,h) for public key, 

                n=p*p*q
                g**(p-1) mod p**2 != 1, 
                h = g**n mod n, 

        @tup : (n,g,h,p,q)
                
                p q are for private key, the factors of n

    """
    def __init__(self,tup):
        "Choose two large distinct primes p and q and compute N = (p**2) * q"
        n,g,h = tup[:3]
        if len(tup) >= 3 :
            self.n = n
            self.g = g
            self.h = h
            self.pubkey = (n,g,h)
        if len(tup) == 5 :
            p, q = tup[3:5]
            self.p = p
            self.q = q
            assert n == pow(p,2) * q, 'Input private key raise error.'
            self.privkey = (g,p,q)
        else :
            raise ValueError('OkamotoUchiyama(tup) : \n\t@tup : \n\t\t(n,g,h) for public key \n\t\t(n,g,h,p,q) for private key')

    def encrypt(self,m):
        """
        return (g ** m * h ** r) % n
        """
        n,g,h = self.pubkey
        r = getRandomRange(1,self.n-1)
        return pow(g,m,n) * pow(h,r,n) % n

    def decrypt(self,c):
        g,p,q = self.privkey
        return self.logarithm(pow(c,p-1,p**2)) * inverse(self.logarithm(pow(g,p-1,p**2)),p)% p
    
    def logarithm(self,x):
        'return L(X) = (X-1) // p'
        return (x-1) // self.p
    
    @classmethod
    def generate(cls,bits):
        p = getPrime(bits//3)
        q = getPrime(bits//3+ bits%3)
        n = p**2 * q
        while True:
            g = getRandomRange(1, n-1)
            g_p = pow(g, p-1, p**2)
            if pow(g_p, p, p**2) == 1:
                break
        h = pow(g,n,n)
        return cls((n,g,h,p,q))

if __name__ == "__main__":
    okamotoUchiyama = OkamotoUchiyama.generate(1024)
    m = getPrime(333)
    c = okamotoUchiyama.encrypt(m)
    assert m == okamotoUchiyama.decrypt(c)