score = float(input("Nhập điểm tổng kết: "))

if 0.0 <= score < 3.0:
    print("Loại Kém")
elif 3.0 <= score < 4.0:
    print("Loại Yếu")
elif 4.0 <= score < 5.0:
    print("Loại Yếu.25")
elif 5.0 <= score < 6.0:
    print("Loại Trung Bình")
elif 6.0 <= score < 7.0:
    print("Loại Khá")
elif 7.0 <= score < 8.0:
    print("Loại Khá")
elif 8.0 <= score < 9.0:
    print("Loại Giỏi")
elif 9.0 <= score <= 10.0:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")