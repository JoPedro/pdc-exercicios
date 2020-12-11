x = int(input())
y = int(input())
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x

for i in range(menor, maior):
    if (i % 5 == 2 or i % 5 == 3) and (i not in (menor, maior)):
        print(i)
