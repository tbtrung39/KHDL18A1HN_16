# Nhập thứ từ người dùng
thu = int(input("Nhập vào thứ (1-7): "))

# Kiểm tra và hiển thị kết quả
if thu == 1:
    print("Thứ 1 là Sunday.")
elif thu == 2:
    print("Thứ 2 là Monday.")
elif thu == 3:
    print("Thứ 3 là Tuesday.")
elif thu == 4:
    print("Thứ 4 là Wednesday.")
elif thu == 5:
    print("Thứ 5 là Thursday.")
elif thu == 6:
    print("Thứ 6 là Friday.")
elif thu == 7:
    print("Thứ 7 là Saturday.")
else:
    print("Thứ không hợp lệ! Vui lòng nhập số từ 1 đến 7.")