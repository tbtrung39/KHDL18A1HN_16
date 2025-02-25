d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
giay =d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print(f"Tổng số giây là: {giay}")