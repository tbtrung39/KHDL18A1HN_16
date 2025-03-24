n = int(input("Nhập số: "))
nhi_phan = ""
if n == 0:
    nhi_phan = "0"
while n > 0:
    nhi_phan = str(n % 2) + nhi_phan
    n = n // 2
print("Dạng nhị phân:", nhi_phan)