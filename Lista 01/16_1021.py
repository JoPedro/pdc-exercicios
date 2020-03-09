valor = float(input())

print("NOTAS:")
print("{0:.0f} nota(s) de R$ 100.00".format(valor // 100))
valor %= 100
print("{0:.0f} nota(s) de R$ 50.00".format(valor // 50))
valor %= 50
print("{0:.0f} nota(s) de R$ 20.00".format(valor // 20))
valor %= 20
print("{0:.0f} nota(s) de R$ 10.00".format(valor // 10))
valor %= 10
print("{0:.0f} nota(s) de R$ 5.00".format(valor // 5))
valor %= 5
print("{0:.0f} nota(s) de R$ 2.00".format(valor // 2))

print("MOEDAS:")
valor %= 2
print("{0:.0f} moeda(s) de R$ 1.00".format(valor // 1))
valor %= 1
print("{0:.0f} moeda(s) de R$ 0.50".format(valor // 0.5))
valor %= 0.5
print("{0:.0f} moeda(s) de R$ 0.25".format(valor // 0.25))
valor %= 0.25
print("{0:.0f} moeda(s) de R$ 0.10".format(valor // 0.1))
valor %= 0.1
print("{0:.0f} moeda(s) de R$ 0.05".format(valor // 0.05))
valor %= 0.05
print("{0:.0f} moeda(s) de R$ 0.01".format(valor / 0.01))
