n = int(input())
la, lb = map(int, input().split())
sa, sb = map(int, input().split())

if la <= n <= lb:
    if sa <= n <= sb:
        print("possivel")
    else:
        print("impossivel")
else:
    print("impossivel")
