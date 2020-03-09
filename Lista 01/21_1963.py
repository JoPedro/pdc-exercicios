a, b = map(float, input().split())

aumento = (b - a) * 100 / a
print("{0:.2f}%".format(aumento))
