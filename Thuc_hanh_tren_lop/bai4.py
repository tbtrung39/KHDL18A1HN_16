t = int(input("Nhập tử số: "))
m = int(input("Nhập mẫu số: "))
while m == 0:
    print("Mẫu số không thể là 0. Vui lòng nhập lại.")
    m = int(input("Nhập mẫu số: "))
print(f"Phân số bạn nhập là: {t}/{m}")
