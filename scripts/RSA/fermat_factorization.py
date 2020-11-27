def nroot(x, n):
    """
    Return truncated n'th root of x.
    """
    if n < 0:
        raise ValueError("can't extract negative root")

    if n == 0:
        raise ValueError("can't extract zero root")

    sign = 1
    if x < 0:
        sign = -1
        x = -x
        if n % 2 == 0:
            raise ValueError("can't extract even root of negative")

    high = 1
    while high ** n <= x:
        high <<= 1

    low = high >> 1
    while low < high:
        mid = (low + high) >> 1
        mr = mid ** n
        if mr == x:
            return (mid, True)
        elif low < mid and mr < x:
            low = mid
        elif high > mid and mr > x:
            high = mid
        else :
            return (sign * mid, False)
    return (sign * (mid + 1) , False)


def fermat_factorization(N) :
    """
    Fermat's factorization for close p and q
    link : https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
    """
    a = nroot(N,2)[0]
    b2 = a*a - N
    b = nroot(N,2)[0]
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - N
        b = nroot(b2,2)[0]
        count += 1
    p=a+b
    q=a-b
    return p, q
