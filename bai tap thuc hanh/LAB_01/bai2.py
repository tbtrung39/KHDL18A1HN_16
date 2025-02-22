ngay = int(input("Nhập số ngày: "))
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
cong_thuc = (ngay * 86400) + (gio * 3600) + (phut * 60) + giay
print("Tổng giá trị: ", cong_thuc)