t = int(input())
for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))

    print(len(list(dict.fromkeys(seq))))