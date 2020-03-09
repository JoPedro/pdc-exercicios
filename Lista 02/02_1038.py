cod, qtd = map(int, input().split())

if cod == 1:
    print("Total: R$ {:.2f}".format(4.00 * qtd))
elif cod == 2:
    print("Total: R$ {:.2f}".format(4.50 * qtd))
elif cod == 3:
    print("Total: R$ {:.2f}".format(5.00 * qtd))
elif cod == 4:
    print("Total: R$ {:.2f}".format(2.00 * qtd))
elif cod == 5:
    print("Total: R$ {:.2f}".format(1.50 * qtd))
