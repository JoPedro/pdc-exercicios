t = int(input())
for i in range(t):
    data = input().split()
    pa, pb = int(data[0]), int(data[1])
    ga, gb = float(data[2]), float(data[3])

    anos = 0
    while pa <= pb:
        pa += (ga * pa) // 100
        pb += (gb * pb) // 100
        anos += 1
        if anos > 100:
            break
    if anos <= 100:
        print(anos, "anos.")
    else:
        print("Mais de 1 seculo.")
    