t = int(input())
a, b, c, d, e = map(int, input().split())

respostas = 0

if a == t:
    respostas += 1
if b == t:
    respostas += 1
if c == t:
    respostas += 1
if d == t:
    respostas += 1
if e == t:
    respostas += 1

print(respostas)
