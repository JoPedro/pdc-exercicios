while True:
    n = int(input())
    if n == 0:
        break
    mag = [int(x) for x in input().split()]
    mag.append(mag[0])
    mag.append(mag[1])
    qtdP = 0
    for i in range(1, n + 1):
        if mag[i] < mag[i - 1] and mag[i] < mag[i + 1]:
            qtdP += 1
        elif mag[i] > mag[i - 1] and mag[i] > mag[i + 1]:
            qtdP += 1
    print(qtdP)