valor = int(input())

horas = valor // 3600
minutos = (valor % 3600) // 60
segundos = ((valor % 3600) % 60) % 60

print(horas, minutos, segundos, sep=":")
