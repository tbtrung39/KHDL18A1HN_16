# Nhập điểm tổng kết của học sinh
diem_tk = float(input("Nhập điểm tổng kết (0.0 - 10.0): "))

# Kiểm tra học lực theo điểm
if 0.0 <= diem_tk <= 3.0:
    print("Loại Kém")
elif diem_tk == 4.0:
    print("Loại Yếu")
elif 5.0 <= diem_tk <= 6.0:
    print("Loại Trung bình")
elif 7.0 <= diem_tk <= 8.0:
    print("Loại Khá")
elif 9.0 <= diem_tk <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ! Vui lòng nhập điểm từ 0.0 đến 10.0.")