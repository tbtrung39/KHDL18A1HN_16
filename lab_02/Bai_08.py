tnct = int(input("Nhập thâm niên công tác (tháng): "))
luong_co_ban = 1350000  # Lương cơ bản

if tnct < 12:
    he_so = 2.34
elif tnct < 36:
    he_so = 3.33
elif tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

luong = he_so * luong_co_ban
print("Lương của nhân viên là:", luong, "đồng")
