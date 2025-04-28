def hoan_vi_de_quy(danh_sach):
  if len(danh_sach) == 0:
    return [[]]
  else:
    hoan_vi = []
    phan_tu_dau = danh_sach[0]
    cac_phan_tu_con_lai = danh_sach[1:]
    cac_hoan_vi_con_lai = hoan_vi_de_quy(cac_phan_tu_con_lai)
    for hoan_vi_con in cac_hoan_vi_con_lai:
      for i in range(len(hoan_vi_con) + 1):
        hoan_vi_moi = hoan_vi_con[:i] + [phan_tu_dau] + hoan_vi_con[i:]
        hoan_vi.append(hoan_vi_moi)
    return hoan_vi

def in_tat_ca_hoan_vi(n):
  day_so = list(range(1, n + 1))
  tat_ca_hoan_vi = hoan_vi_de_quy(day_so)
  print(f"Tất cả các hoán vị của dãy [1, 2, ..., {n}] là:")
  for hoan_vi in tat_ca_hoan_vi:
    print(hoan_vi)
n = int(input("Nhập số tự nhiên n: "))
in_tat_ca_hoan_vi(n)