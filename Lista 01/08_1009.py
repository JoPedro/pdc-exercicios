nome = input()
salario = float(input())
vendas = float(input())

bonus = salario + vendas * 0.15
print("TOTAL = R$ {0:.2f}".format(bonus))
