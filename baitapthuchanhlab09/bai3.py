def luy_thua_de_quy(a, n):
  if n == 0:
    return 1
  elif n == 1:
    return a
  
  elif n % 2 == 0:
    nua_n = n // 2
    return luy_thua_de_quy(a, nua_n) * luy_thua_de_quy(a, nua_n)
  else:
    return a * luy_thua_de_quy(a, n - 1)
co_so = float(input("Nhập cơ số a: "))
so_mu = int(input("Nhập số mũ n (không âm): "))
if so_mu < 0:
  print("Số mũ phải là một số nguyên không âm.")
else:
  ket_qua = luy_thua_de_quy(co_so, so_mu)
  print(f"{co_so} mũ {so_mu} bằng: {ket_qua}")