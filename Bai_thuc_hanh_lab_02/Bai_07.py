diem = float(input("Nhập học lực của học sinh: "))
if 0.0 <= diem <= 3.0:
    print("Loại kém")
elif diem == 4.0:
    print("Loại yếu")
elif 5.0 <= diem <= 6.0:
    print("Loại trung bình")
elif 7.0 <= diem <= 8.0:
    print("Loại khá")
elif 9.0 <= diem <= 10:
    print("Loại giỏi")
else:
    print("Nhập sai vui lòng nhập lại")