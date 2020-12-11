n = int(input())
string = ''
fibo = []
for i in range(n):
    if i == 0:
        fibo.append(0)
        string += '0'
    elif i == 1:
        fibo.append(1)
        string += ' 1'
    else:
        fibo.append(fibo[i - 1] + fibo[i - 2])
        string += ' ' + str(fibo[len(fibo) - 1])
print(string)