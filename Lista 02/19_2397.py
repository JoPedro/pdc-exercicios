a, b, c = map(int, input().split())

if ((b - c) * -1) < a < b + c and ((a - c) * -1) < b < a + c and ((a - b) * -1) < c < a + b:
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        print("r")
    elif a ** 2 < b ** 2 + c ** 2 or b ** 2 < a ** 2 + c ** 2 or c ** 2 < b ** 2 + a ** 2:
        print("a")
    elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > a ** 2 + c ** 2 or c ** 2 > b ** 2 + a ** 2:
        print("o")
else:
    print("n")
