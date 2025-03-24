nhi_phan = input("Nhập số nhị phân: ")
thap_phan = 0
length = len(nhi_phan)

for i in range(length):
    thap_phan += int(nhi_phan[i]) * (2 ** (length - i - 1))

print("Số thập phân:", thap_phan)