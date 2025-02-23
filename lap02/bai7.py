diem_tk = float(input("Nhập điểm TK: "))

if 0.0 <= diem_tk <= 3.0:
    hoc_luc = "Loại Kém"
elif diem_tk == 4.0:
    hoc_luc = "Loại Yếu"
elif 5.0 <= diem_tk <= 6.0:
    hoc_luc = "Loại Trung bình"
elif 7.0 <= diem_tk <= 8.0:
    hoc_luc = "Loại Khá"
elif 9.0 <= diem_tk <= 10.0:
    hoc_luc = "Loại Giỏi"
else:
    hoc_luc = "Điểm không hợp lệ"

print(f"Học lực: {hoc_luc}")