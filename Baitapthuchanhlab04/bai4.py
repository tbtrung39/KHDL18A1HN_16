tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

while mau_so == 0:
    print("Mẫu số phải khác 0. Nhập lại.")
    mau_so = int(input("Nhập mẫu số: "))

print("Phân số:", tu_so, "/", mau_so)
