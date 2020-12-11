while True:
    horas = [int(i) for i in input().split()]
    if horas[0] == 0 and horas[1] == 0 and horas[2] == 0 and horas[3] == 0:
        break
    min1 = horas[0] * 60 + horas[1]
    min2 = horas[2] * 60 + horas[3]
    if min2 - min1 < 0:
        print(1440 - (abs(min2 - min1)))
    else:
        print(min2 - min1)
