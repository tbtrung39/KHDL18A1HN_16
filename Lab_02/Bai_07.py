diem_tk = float(input("Nhập điểm tổng kết: "))

if 0.0 <= diem_tk <= 3.0:
    hoc_luc = "Kém"
elif diem_tk == 4.0:
    hoc_luc = "Yếu"
elif 5.0 <= diem_tk <= 6.0:
    hoc_luc = "Trung bình"
elif 7.0 <= diem_tk <= 8.0:
    hoc_luc = "Khá"
elif 9.0 <= diem_tk <= 10.0:
    hoc_luc = "Giỏi"
else:
    hoc_luc = "Điểm không hợp lệ"

print("Học lực của học sinh là:", hoc_luc)