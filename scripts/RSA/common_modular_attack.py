
def common_modular(set1,set2):
    """
    Common Modular Attack, if you get c1 = m^e1 % N , c2 = m^e2 % N
        Given two set of ( N, e, c )
        return plaintext
    """
    n1,e1,c1 = set1 
    n2,e2,c2 = set2 
    if n1 != n2 : 
        print("[-] Common Modular Attack Fail, n1 != n2")
        return
    if gcd(e1,e2) != 1 : 
        print("[-] Common Modular Attack Fail, gcd(e1,e2) != 1")
        return
    a,b = xgcd(e1,e2)
    t1 = pow(c1,abs(a),n1)
    t2 = pow(c2,abs(b),n2)
    if a < 0 : t1 = invmod(t1,n1)
    if b < 0 : t2 = invmod(t2,n2)
    return t1*t2 % n1
    