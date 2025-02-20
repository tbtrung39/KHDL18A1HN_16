diem_TK = float(input("Nhập vào điểm tổng kết: "))
if 0.0 <= diem_TK <= 3.0:
    print("học sinh xếp loại kém.")
elif diem_TK == 4.0:
    print("học sinh xếp loại yếu.")
elif 5.0 <= diem_TK <= 6.0:
    print("học sinh xếp loại trung bình.")
elif 7.0 <= diem_TK <= 8.0:
    print("học sinh xếp loại khá.")
elif 9.0 <= diem_TK <= 10.0:
    print("học sinh xếp loại giỏi.")
else:
    print("Nhập điểm TK sai, vui lòng nhập lại.")
