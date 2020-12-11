n = int(input())
for i in range(n):
    x = int(input())
    primo = True
    for j in range(1, x + 1):
        if x % j == 0 and j not in (1, x):
            primo = False
            break
    if primo:
        print(x, 'eh primo')
    else:
        print(x, 'nao eh primo')
        