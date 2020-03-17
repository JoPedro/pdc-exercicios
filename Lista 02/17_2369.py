n = int(input())
consumo = 7

if 10 < n <= 30:
    consumo += (n - 10)
elif 30 < n <= 100:
    consumo += ((n - 30) * 2) + 20
elif n > 100:
    consumo += ((n - 100) * 5) + 160

print(consumo)
