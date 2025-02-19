
d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
tong_giay = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print("Tổng thời gian quy đổi thành giây là:", tong_giay, "giây")