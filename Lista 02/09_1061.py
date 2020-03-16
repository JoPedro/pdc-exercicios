k, dd_init = input().split()
hh_init, mm_init, ss_init = map(int,input().split(":"))
j, dd_final = input().split()
hh_final, mm_final, ss_final = map(int,input().split(":"))
dd_init = int(dd_init)
dd_final = int(dd_final)

qtd_seg_final = (dd_final * 86400) + (hh_final * 3600) + (mm_final * 60) + ss_final
qtd_seg_init = (dd_init * 86400) + (hh_init * 3600) + (mm_init * 60) + ss_init

qtd_seg = qtd_seg_final - qtd_seg_init

print("{} dia(s)".format(qtd_seg // 86400))
qtd_seg %= 86400
print("{} hora(s)".format(qtd_seg // 3600))
qtd_seg %= 3600
print("{} minuto(s)".format(qtd_seg // 60))
qtd_seg %= 60
print("{} segundo(s)".format(qtd_seg % 60))
