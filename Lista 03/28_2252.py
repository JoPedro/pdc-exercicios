teste = 1
while True:
    try:
        n = int(input())
        oleo = [float(x) for x in input().split()]
        senha = []
        for i in range(n):
            senha.append(oleo.index(max(oleo)))
            oleo.insert(oleo.index(max(oleo)), -1)
            oleo.remove(max(oleo))
        print('Caso ', teste, ": ", *senha, sep='')
        teste += 1

    except EOFError:
        break