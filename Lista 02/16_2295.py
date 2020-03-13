a, g, ra, rg = map(float, input().split())

preco_a = a * ra
preco_g = g * rg

if preco_g <= preco_a or a == g:
    print("G")
else:
    print("A")
