idades = []
while True:
    idade = int(input())
    if idade < 0:
        break
    idades.append(idade)
print("{:.2f}".format(sum(idades) / len(idades)))
