print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
chon = 0
while chon < 1 or chon > 5:
    chon = int(input("Nhập số tương ứng với đồ uống bạn muốn chọn (1-5): "))
ten_do_uong = ""
if chon == 1:
    ten_do_uong = "Cafe"
if chon == 2:
    ten_do_uong = "Cam vắt"
if chon == 3:
    ten_do_uong = "Nước ép cà rốt"
if chon == 4:
    ten_do_uong = "Nước lọc"
if chon == 5:
    ten_do_uong = "Nước dừa"
print("Bạn đã chọn:", ten_do_uong)
