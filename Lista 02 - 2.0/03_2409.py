a, b, c = map(int, input().split())
h, l = map(int, input().split())

if (b <= h and c <= l) or (c <= h and b <= l) or (c <= h and a <= l) or (a <= h and c <= l) or (a <= h and b <= l) or (b <= h and a <= l):
    print("S")
else:
    print("N")
