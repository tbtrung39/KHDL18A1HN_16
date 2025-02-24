# Khai báo lương căn bản
luong_cb = 1350000  

# Nhập số tháng thâm niên công tác
tnct = int(input("Nhập số tháng thâm niên công tác: "))

# Xác định hệ số lương dựa trên TNCT
if tnct < 12:
    he_so = 2.34
elif 12 <= tnct < 36:
    he_so = 3.33
elif 36 <= tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99

# Tính lương
luong = he_so * luong_cb  

# Xuất kết quả
print("Lương của nhân viên là:", int(luong), "đồng")