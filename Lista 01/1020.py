valor = int(input())

anos = valor // 365
print(anos, "ano(s)")
mes = (valor % 365) // 30
print(mes, "mes(es)")
dias = (valor % 365) % 30
print(dias, "dia(s)")
