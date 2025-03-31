nhat_ky = []
while True:
  giao_dich = input("Nhập giao dịch (D 100 hoặc W 200): ")
  if not giao_dich:
    break
  nhat_ky.append(giao_dich)

so_du = 0
for giao_dich in nhat_ky:
  loai, tien = giao_dich.split()
  tien = int(tien)
  if loai == 'D':
    so_du += tien
  elif loai == 'W':
    so_du -= tien

print("Số dư:", so_du)