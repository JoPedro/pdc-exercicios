dia_init = input()
h_init = input()
dia_final = input()
h_final = input()

dd_final = int(dia_final[-1:])
dd_init = int(dia_init[-1:])
hh_final = int(h_final[:2])
hh_init = int(h_init[:2])
mm_final = int(h_final[5:-5])
mm_init = int(h_init[5:-5])
ss_final = int(h_final[-2:])
ss_init = int(h_init[-2:])

if dd_final > dd_init:
    print("{} dia(s)".format(dd_final - (dd_init + 1)))
else:
    print("0 dia(s)")

if hh_final > hh_init:
    print("{} hora(s)".format(hh_final - hh_init))  
elif hh_final < hh_init:
    print("{} hora(s)".format(24 - hh_init + hh_final))
else:
    print("0 hora(s)")

if mm_final > mm_init:
    print("{} minuto(s)".format(mm_final - mm_init))
elif mm_final < mm_init:
    print("{} minuto(s)".format(60 - mm_init + mm_final))

if ss_final > ss_init:
    print("{} segundo(s)".format(ss_final - ss_init))
elif ss_final < ss_init:
    print("{} segundo(s)".format(60 - ss_init + ss_final))
else:
    print("0 segundo(s)")
