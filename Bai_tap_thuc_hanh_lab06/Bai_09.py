# Nhập danh sách các số tự nhiên
lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

# Kiểm tra tất cả các số trong danh sách có phải là số chẵn không
for num in lst:
    assert num % 2 == 0, f"Số {num} không phải là số chẵn!"

print("Tất cả các số trong danh sách đều là số chẵn.")
