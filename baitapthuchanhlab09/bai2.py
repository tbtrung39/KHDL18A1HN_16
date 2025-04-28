def ucln_hai_so(a, b):
  while b:
    a, b = b, a % b
  return a
def ucln_nhieu_so(danh_sach_so):
  if not danh_sach_so:
    return 0 
  elif len(danh_sach_so) == 1:
    return danh_sach_so[0]
  else:
    ucln_chung = ucln_hai_so(danh_sach_so[0], danh_sach_so[1])
    for i in range(2, len(danh_sach_so)):
      ucln_chung = ucln_hai_so(ucln_chung, danh_sach_so[i])
    return ucln_chung
n = int(input("Nhập số lượng số n: "))
cac_so = []
for i in range(n):
  so = int(input(f"Nhập số thứ {i+1}: "))
  cac_so.append(so)
ucln_cua_cac_so = ucln_nhieu_so(cac_so)
print(f"Ước chung lớn nhất của các số đã nhập là: {ucln_cua_cac_so}")