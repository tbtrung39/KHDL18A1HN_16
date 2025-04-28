def giai_thua_kep(n):
  if not isinstance(n, int) or n < 0:
    print("Lỗi: n phải là một số nguyên không âm.")
    return None
  if n == 0 or n == 1:
    return 1
  else:
    result = 1
    for i in range(n, 0, -2):
      result *= i
    return result
def tinh_tong_s(gioi_han=1000):
  tong_s = 0
  for k in range(1, gioi_han):
    term = giai_thua_kep(k)
    if term is None:  
      break
    sign = 1 if (k - 1) % 2 == 0 else -1
    tong_s += sign * term
  return tong_s
# Ví dụ 
n_example = 5
giai_thua_kep_n = giai_thua_kep(n_example)
if giai_thua_kep_n is not None:
  print(f"{n_example}!! = {giai_thua_kep_n}")