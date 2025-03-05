# Nhập giá trị từ bàn phím
s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

# Đổi tất cả về giây
tong_giay = s + m * 60 + h * 3600 + d * 86400

# In kết quả
print("Tổng số giây:", tong_giay)