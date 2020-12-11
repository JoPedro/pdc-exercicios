while True:
    x = int(input())
    if x == 0:
        break
    seq = '1'
    for i in range(2, x + 1):
        seq += ' ' + str(i)
    print(seq)