n, m = input().split()
while n != '0' or m != '0':
    n = list(n)
    m = list(m)
    n_alg = list(map(int, n))
    m_alg = list(map(int, m))
    while sum(n_alg) > 9:
        n_alg = list(map(int, list(str(sum(n_alg)))))
    while sum(m_alg) > 9:
        m_alg = list(map(int, list(str(sum(m_alg)))))    
    if sum(n_alg) > sum(m_alg):
        print(1)
    elif sum(n_alg) < sum(m_alg):
        print(2)
    elif sum(n_alg) == sum(m_alg):
        print(0)
    n, m = input().split()
