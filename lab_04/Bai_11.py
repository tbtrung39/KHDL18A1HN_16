
print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
chon = int(input("Nhập số tương ứng với loại đồ uống bạn muốn gọi: "))
if chon == 1:
    print("Bạn đã chọn Cafe.")
elif chon == 2:
    print("Bạn đã chọn Cam vắt.")
elif chon == 3:
    print("Bạn đã chọn Nước ép cà rốt.")
elif chon == 4:
    print("Bạn đã chọn Nước lọc.")
elif chon == 5:
    print("Bạn đã chọn Nước dừa.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn số từ 1 đến 5.")