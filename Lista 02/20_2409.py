a, b, c = map(int, input().split())
h, l = map(int, input().split())

if ((a > h and a > l) and (b > h and b > l)) or ((a > h and a > l) and (c > h and c > l)) or ((c > h and c > l) and (b > h and b > l)):
    print("N")
else:
    print("S")