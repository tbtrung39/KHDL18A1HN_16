def tim_so_lon_nhat(so_thu_nhat, so_thu_hai, so_thu_ba):
  so_lon_nhat = max(so_thu_nhat, so_thu_hai, so_thu_ba)
  return so_lon_nhat
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))
so_lon_nhat_tim_duoc = tim_so_lon_nhat(num1, num2, num3)
print(f"Số lớn nhất trong ba số {num1}, {num2} và {num3} là: {so_lon_nhat_tim_duoc}")