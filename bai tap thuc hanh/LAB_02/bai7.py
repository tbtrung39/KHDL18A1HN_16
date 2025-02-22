diem = float(input("Nhập điểm tổng kết: "))
if 0.0 <= diem <= 3.0:
    print("Xếp loại: Kém")
elif diem == 4.0:
    print("Xếp loại Yếu")
elif 5.0 <= diem <= 6.0:
    print("Xếp loại Trung bình")
elif 7.0 <= diem <= 8.0:
    print("Xếp loại Khá")
elif 9.0 <= diem <= 10.0:
    print("Xếp loại Giỏi")
else:
    print("Vui lòng nhập lại điểm")