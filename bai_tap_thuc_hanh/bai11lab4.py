print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

choice = int(input("Nhập số để chọn đồ uống: "))

while choice < 1 or choice > 5:
    print("Lựa chọn không hợp lệ, hãy nhập lại!")
    choice = int(input("Nhập số để chọn đồ uống: "))

if choice == 1:
    print("Bạn đã chọn: Cafe")
elif choice == 2:
    print("Bạn đã chọn: Cam vắt")
elif choice == 3:
    print("Bạn đã chọn: Nước ép cà rốt")
elif choice == 4:
    print("Bạn đã chọn: Nước lọc")
elif choice == 5:
    print("Bạn đã chọn: Nước dừa")