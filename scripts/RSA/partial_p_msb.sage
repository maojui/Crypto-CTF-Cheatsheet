"Find P with only knowning 50% of MSB (least significant bit)"

def recover_lsb(n, p, debug=False) :
    beta = 0.5
    epsilon = beta^2/7
    kbits = floor(n.nbits()*(beta^2-epsilon))
    PR.<x> = PolynomialRing(Zmod(n))
    f = x + p
    x0 = f.small_roots(X=2^kbits, beta=0.3)[0]  # find root < 2^kbits with factor >= n^0.3
    return x0

if __name__ == "__main__":
    # # Testing
    # p = random_prime(2^512-1,True,2^511)
    # q = random_prime(2^512-1,True,2^511)
    # n = p*q
    # pbits = p.nbits()
    # kbits = floor(n.nbits()*(beta^2-epsilon))
    # partial_p = p & (2^pbits-2^kbits)
    # print("upper %d bits (of %d bits) given" % (pbits-kbits, pbits))
    # x0 = recover_lsb(n, partial_p)

    # Usage 
    n = 144577323082341606781087333127652195614928653924628840063283124688666697172079299540987986466905508888459466234427758008685453349603672093268364681219809070052759188387414913364503551677980960440032525534198537772481074574240349700392333150907937512241296276227852496435058553681077786863331924405426219248647
    partial_p = 11043285040234897370108230348414076720909958796181348046213933603334639323065878778927432781023976397098528035583181448962487564184116786691066219045322752
    x0 = recover_lsb(n, partial_p)
    print(f"known: {partial_p}")
    print(f"Missing LSB: {x0}")
    print(f"p = {x0 + partial_p}")
    print(f"isPrime: {is_prime(x0 + partial_p)}")