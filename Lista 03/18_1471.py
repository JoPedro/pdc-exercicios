while True:
    try:
        n, r = map(int, input().split())
        vol = list(map(int, input().split()))
        rip = []
        for i in range(1, n + 1):
            rip.append(i)
        if len(rip) == len(vol):
            print('*')
        else:
            for i in rip:
                if vol.index(i) >= 0:
                    rip.remove(i)
            print(*rip)
    except EOFError:
        break
