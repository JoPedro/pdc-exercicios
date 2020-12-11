teste = 1
n = int(input())
while (n != 0):
    x1, y1, u1, v1 = -10000, 10000, 10000, -10000
    for i in range(n):
        x, y, u, v = map(int, input().split())
        x1, y1, u1, v1 = max(x, x1), min(y1, y), min(u, u1), max(v1, v)
    print('Teste', teste)
    teste += 1
    if x1 <= u1 and y1 >= v1:
        print (x1, y1, u1, v1)
    else:
        print('nenhum')
    print()
    n = int(input())