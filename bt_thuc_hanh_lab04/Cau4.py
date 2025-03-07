# Câu 4
while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so == 0:
        print("Mẫu số không được bằng 0, vui lòng nhập lại!")
    else:
        break
print(f"Phân số là: {tu_so}/{mau_so}")