# Hiển thị menu đồ uống
print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

# Khởi tạo biến lựa chọn
chon = 0

# Dùng vòng lặp để yêu cầu người dùng chọn đúng số trong menu
while chon < 1 or chon > 5:
    print("Nhập số tương ứng với đồ uống bạn muốn gọi (1-5):")
    chon = int(input())

    if chon < 1 or chon > 5:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

# Xác định đồ uống đã chọn và hiển thị kết quả
if chon == 1:
    do_uong = "Cafe"
elif chon == 2:
    do_uong = "Cam vắt"
elif chon == 3:
    do_uong = "Nước ép cà rốt"
elif chon == 4:
    do_uong = "Nước lọc"
else:
    do_uong = "Nước dừa"

print("Bạn đã chọn:", do_uong)