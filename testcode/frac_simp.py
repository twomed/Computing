o = input('Numerator:')
p = input('Denominator:')


def div(n, q):
    if n % q == 0:
        return q


def frac_simp(n, m):
    """ This is a function that simplifies fractions"""
    n = int(n)
    m = int(m)
    n_list = []
    m_list = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    for i in primes:
        w = 1
        num = n
        while div(num, i) is not None:
            n_list.append(i)
            num = num / i
            w += 1
    for k in primes:
        w = 1
        num = m
        while div(num, k) is not None:
            m_list.append(k)
            num = num / k
            w += 1

    print(n_list)
    print(m_list)

    for elm in n_list and m_list:
        n_list.remove(elm)
        m_list.remove(elm)

    print(n_list)
    print(m_list)



frac_simp(o, p)
