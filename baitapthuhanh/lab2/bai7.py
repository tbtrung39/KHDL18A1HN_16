score = float(input("Nhập điểm: "))
if 0 <= score < 3:
    print("Loại Kém")
elif score == 4:
    print("Loại Yếu.25")
elif 5 <= score < 7:
    print("Loại Trung Bình")
elif 7 <= score < 9:
    print("Loại Khá")
elif score >= 9:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ.")