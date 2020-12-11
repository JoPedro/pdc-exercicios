qtd = int(input())
num = []

for i in range(qtd):
    n = int(input())
    num.append(n)

for i in range(len(num)):
    if num[i] == 0:
        print('NULL')
    if (num[i] % 2 == 0) and (num[i] > 0):
        print('EVEN POSITIVE')
    if (num[i] % 2 == 0) and (num[i] < 0):
        print('EVEN NEGATIVE')
    if (num[i] % 2 != 0) and (num[i] > 0):
        print('ODD POSITIVE')
    if (num[i] % 2 != 0) and (num[i] < 0):
        print('ODD NEGATIVE')
