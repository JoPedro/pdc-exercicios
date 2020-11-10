a1 = int(input())
a2 = int(input())
a3 = int(input())

t1 = a2 * 2 + a3 * 4
t2 = a1 * 2 + a3 * 2
t3 = a1 * 4 + a2 * 2

if t1 <= t2 and t1 <= t3:
    print(t1)
elif t2 <= t3:
    print(t2)
else:
    print(t3)
