import math

class LSBOracle:

    def __init__(self, n, c, e, oracle_modulus=2):
        """
            n is the module,
        """
        self.upper_bound = n
        self.lower_bound = 0
        self.n = n 
        self.e = e 
        self.c = c 
        self.counter = 0
        self.modulus = oracle_modulus
    
    def set_modulus(self, oracle_modulus):
        self.modulus = oracle_modulus

    def update_bound(self, bits_val):
        jump = self.modulus
        for i in range(jump):
            if bits_val == ((-self.n * i) % jump) :
                upper_bound = self.upper_bound
                lower_bound = self.lower_bound
                self.upper_bound = lower_bound + ((upper_bound - lower_bound) * (i + 1) // jump + 1)
                self.lower_bound = lower_bound + ((upper_bound - lower_bound) * i // jump)
            print(f'bound: {self.lower_bound} ~ {self.upper_bound})')

    def get_bound(self):
        return (self.upper_bound,self.lower_bound)

    def set_bound(self,bound):
        self.upper_bound, self.lower_bound = bound

    def history(self):
        return self.history
        
    def start(self):
        mul = pow(self.modulus, self.e, self.n)
        try :
            for _ in range(self.counter, int(math.log(self.n, self.modulus))):
                c = (mul * self.c) % self.n
                bits_val = self.oracle(c)
                self.update_bound(bits_val)
                self.c = c
                self.counter += self.modulus
        except Exception as e:
            print(e)
            print("Something stop Finding ...")
        print(f'bound: {self.lower_bound} ~ {self.upper_bound})')

    def oracle(self, c):
        raise NotImplementedError


if __name__ == "__main__":
    
    # Example
    
    from pwn import *

    r = remote('localhost', 10000)
    n = int(r.recvline().strip(b'n = ').strip())
    c = int(r.recvline().strip(b'c = ').strip())
    e = 65537
    
    def oracle(c):
        r.sendline(str(c))
        return int(r.recvline().strip(b'm % 3 = ').strip())
        
    lsb = LSBOracle(n,c,e,3)
    lsb.oracle = oracle
    lsb.start()