p_init, p_final = map(int, input().split())

if 0 <= p_final <= 2:
    print("nova")
if 96 < p_final <= 100:
    print("cheia")

if p_final > p_init:
    if 2 < p_final <= 96:
        print("crescente")
else:
    if 2 < p_final <= 96:
        print("minguante")
