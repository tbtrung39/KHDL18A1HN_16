nhi_phan = input("Nhập chuỗi nhị phân: ")
thap_phan = 0
for i in range(len(nhi_phan)):
    thap_phan += int(nhi_phan[len(nhi_phan) - 1 - i]) * (2 ** i)
print("Số thập phân tương ứng:", thap_phan)