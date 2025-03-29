tong = 0
while True:
    dong = input("Nhập giao dịch (D hoặc W và số, enter để dừng): ")
    if dong == "":
        break
    # Tách chuỗi thành ký tự và số
    loai = ""
    so = ""
    for i in dong:
        if i.isalpha():
            loai += i
        elif i.isdigit():
            so += i
    so = int(so)
    if loai == "D":
        tong += so
    elif loai == "W":
        tong -= so

print("Tổng tiền còn lại:", tong)
