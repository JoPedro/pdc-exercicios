h_init, h_final = map(int, input().split())

if h_final > h_init:
    print("O JOGO DUROU {} HORA(S)".format(h_final - h_init))
elif h_final < h_init:
    print("O JOGO DUROU {} HORA(S)".format(24 - h_init + h_final))
else:
    print("O JOGO DUROU 24 HORA(S)")
