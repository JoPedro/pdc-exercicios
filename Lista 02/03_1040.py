n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

if media >= 7.0:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame:", ne)
    mf = (ne + media) / 2

    if mf >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(mf))
