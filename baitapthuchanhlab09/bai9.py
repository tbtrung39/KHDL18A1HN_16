def dao_nguoc_so(n):
  if not isinstance(n, int) or n <= 0:
    print("Lỗi: Đầu vào phải là một số nguyên dương.")
    return None
  so_dao_nguoc = 0
  while n > 0:
    chu_so_cuoi = n % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi
    n //= 10
  return so_dao_nguoc
# Ví dụ 
so_nhap = 12345
so_dao = dao_nguoc_so(so_nhap)
if so_dao is not None:
  print(f"Nhập vào: {so_nhap}; in ra: {so_dao}")