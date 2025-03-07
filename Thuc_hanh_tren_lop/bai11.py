menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("Menu đồ uống:")
for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")
while True:
    choice = int(input("Chọn đồ uống (1-5): "))
    if 1 <= choice <= 5:
        print(f"Bạn đã chọn: {menu[choice - 1]}")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")



