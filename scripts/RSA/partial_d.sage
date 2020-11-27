# partial_d.sage
def partial_p(p0, kbits, n):
    PR.<x> = PolynomialRing(Zmod(n))
    nbits = n.nbits()
    f = 2^kbits*x + p0
    f = f.monic()
    roots = f.small_roots(X=2^(nbits//2-kbits), beta=0.3)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3
    if roots:
        x0 = roots[0]
        p = gcd(2^kbits*x0 + p0, n)
        return ZZ(p)

def find_p(d0, kbits, e, n):
    P = var('P')
    for k in range(1, e+1):
        results = solve_mod([e*d0*P - k*(n-P+1)*P + k*n == P], 2^kbits)
        for x in results:
            p0 = ZZ(x[0])
            p = partial_p(p0, kbits, n)
            if p:
                return p

if __name__ == '__main__':
    print("start!")
    n = 123541066875660402939610015253549618669091153006444623444081648798612931426804474097249983622908131771026653322601466480170685973651622700515979315988600405563682920330486664845273165214922371767569956347920192959023447480720231820595590003596802409832935911909527048717061219934819426128006895966231433690709
    e = 97
    nbits = n.nbits()
    kbits = 300
    d0 = 48553333005218622988737502487331247543207235050962932759743329631099614121360173210513133
    print("lower %d bits (of %d bits) is given" % (kbits, nbits))

    p = find_p(d0, kbits, e, n)
    print("found p: %d" % p)