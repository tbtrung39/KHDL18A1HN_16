a = list(map(int, input("Nhập danh sách số cách nhau bằng dấu cách: ").split()))
for num in a:
    assert num % 2 == 0, f"Số {num} không phải số chẵn"
print("Tất cả số trong danh sách đều là số chẵn")