so_n = int(input("Nhập số tự nhiên n: "))
nhi_phan = ""
while so_n > 0:
    nhi_phan = str(so_n % 2) + nhi_phan
    so_n //= 2
print("Số nhị phân tương ứng là:", nhi_phan)