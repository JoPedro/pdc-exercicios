while True:
    h = int(input())
    if h == 0:
        break
    granizo = [h]
    for i in granizo:
        if granizo[len(granizo) - 1] == 1:
            break
        if granizo[granizo.index(i)] % 2 == 0:
            granizo.append(granizo[granizo.index(i)] // 2)
        else:
            granizo.append(granizo[granizo.index(i)] * 3 + 1)
    print(max(granizo))