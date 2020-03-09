a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

qtd = (x // a) * (y // b) * (z // c)
print(qtd)
