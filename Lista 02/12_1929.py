a, b, c, d = map(int, input().split())

if ((b - c) * -1) < a < b + c and ((a - c) * -1) < b < a + c and ((a - b) * -1) < c < a + b:
    print("S")
elif ((b - d) * -1) < a < b + d and ((a - d) * -1) < b < a + d and ((a - b) * -1) < d < a + b:
    print("S")
elif ((c - d) * -1) < a < c + d and ((a - d) * -1) < c < a + d and ((a - c) * -1) < d < a + c:
    print("S")
elif ((c - d) * -1) < b < c + d and ((b - d) * -1) < c < b + d and ((b - c) * -1) < d < b + c:
    print("S")
else:
    print("N")
