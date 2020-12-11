n = int(input())
l = [None] * n
l = list(map(int, input().split()))
print('Menor valor:', min(l))
print('Posicao:', l.index(min(l)))