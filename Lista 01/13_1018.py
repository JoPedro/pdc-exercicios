valor = int(input())
print(valor)

cem = valor // 100
print(cem, "nota(s) de R$ 100,00")
cinquenta = (valor % 100) // 50
print(cinquenta, "nota(s) de R$ 50,00")
vinte = ((valor % 100) % 50) // 20
print(vinte, "nota(s) de R$ 20,00")
dez = (((valor % 100) % 50) % 20) // 10
print(dez, "nota(s) de R$ 10,00")
cinco = ((((valor % 100) % 50) % 20) % 10) // 5
print(cinco, "nota(s) de R$ 5,00")
dois = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
print(dois, "nota(s) de R$ 2,00")
um = (((((valor % 100) % 50) % 20) % 10) % 5) % 2
print(um, "nota(s) de R$ 1,00")
