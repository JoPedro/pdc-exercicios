l, d = map(int, input().split())
k, p = map(int, input().split())

custo = (l * k) + (p * (l // d))
print(custo)
