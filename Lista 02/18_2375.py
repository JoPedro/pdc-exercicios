db = int(input())
a, l, p = map(int, input().split())

if db <= a and db <= l and db <= p:
    print("S")
else:
    print("N")
