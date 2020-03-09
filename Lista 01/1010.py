cod1, n1, valor1 = input().split()
cod1 = int(cod1)
n1 = int(n1)
valor1 = float(valor1)

cod2, n2, valor2 = input().split()
cod2 = int(cod2)
n2 = int(n2)
valor2 = float(valor2)

valor = (n1 * valor1) + (n2 * valor2)
print("VALOR A PAGAR: R$ {0:.2f}".format(valor))
