# a) S = 1/(1*2) + 1/(2*3) + ... + 1/(n*(n+1))
def tinh_tong_a(n):
  if not isinstance(n, int) or n <= 0:
    return "Đầu vào phải là một số nguyên dương."
  tong = 0
  for i in range(1, n + 1):
    tong += 1 / (i * (i + 1))
  return tong
# b) S = 1/1! + 1/2! + 1/3! + ... + 1/n! (không dùng math.factorial)
def tinh_tong_b(n):
  if not isinstance(n, int) or n <= 0:
    return "Đầu vào phải là một số nguyên dương."
  tong = 0
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
    tong += 1 / factorial
  return tong
# c) S = căn bậc hai(3 + căn bậc hai(6 + căn bậc hai(9 + ... + căn bậc hai(3n))))
import math 
def tinh_tong_c(n):
  if not isinstance(n, int) or n <= 0:
    return "Đầu vào phải là một số nguyên dương."
  ket_qua = 0
  for i in range(n, 0, -1):
    ket_qua = math.sqrt(3 * i + ket_qua)
  return ket_qua
# Ví dụ
n_a = 5
tong_a = tinh_tong_a(n_a)
print(f"Tổng của chuỗi a) với n = {n_a} là: {tong_a}")
n_b = 4
tong_b = tinh_tong_b(n_b)
print(f"Tổng của chuỗi b) với n = {n_b}là: {tong_b}")
n_c = 4
tong_c = tinh_tong_c(n_c)
print(f"Giá trị của chuỗi c) với n = {n_c} là: {tong_c}")
#d 
import math
def tinh_s_phan_d(n):
    if not isinstance(n, int) or n <= 0:
        print("Lỗi: n phải là một số nguyên dương.")
        return None
    if n == 1:
        print("Lỗi: Biểu thức không xác định cho n = 1.")
        return None
    gia_tri_ben_trong = 1.0
    for i in range(2, n + 1):
        gia_tri_ben_trong = pow(i + gia_tri_ben_trong, 1 / (i - 1))
    s = pow(n + gia_tri_ben_trong, 1 / (n + 1))
    return s
# Ví dụ 
gia_tri_n = 2
ket_qua_s = tinh_s_phan_d(gia_tri_n)
if ket_qua_s is not None:
    print(f"Giá trị gần đúng của S khi n = {gia_tri_n} là: {ket_qua_s}")