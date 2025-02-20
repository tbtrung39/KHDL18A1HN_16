thamnien = int(input("Nhập số tháng làm việc: "))

if thamnien < 12:
    he_so = 2.34
elif thamnien < 36:
    he_so = 3.33
elif thamnien < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong_can_ban = 1350000
luong = he_so * luong_can_ban

print("Lương của nhân viên là:", luong, "đồng")