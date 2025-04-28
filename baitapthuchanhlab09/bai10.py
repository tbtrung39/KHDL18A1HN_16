def tinh_xn(n):
  if not isinstance(n, int) or n < 0:
    print("Lỗi: n phải là một số nguyên không âm.")
    return None
  if n == 0:
    return 1 
  xn = 0
  for k in range(n):
    term = (n - k)**2
    if k == 0:
      term *= tinh_xn(0)
    else:
      term *= tinh_xn(k)
    xn += term
  return xn
# Ví dụ 
print(f"X0 = {tinh_xn(0)}")