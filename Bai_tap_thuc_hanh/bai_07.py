diem = float(input("Nhập điểm tổng kết: "))

if 0.0 <= diem <= 3.0:
    hoc_luc = "Kém"
elif diem == 4.0:
    hoc_luc = "Yếu"
elif 5.0 <= diem <= 6.0:
    hoc_luc = "Trung bình"
elif 7.0 <= diem <= 8.0:
    hoc_luc = "Khá"
elif 9.0 <= diem <= 10.0:
    hoc_luc = "Giỏi"
else:
    hoc_luc = "Điểm không hợp lệ"

print(f"Học lực của học sinh là: {hoc_luc}")