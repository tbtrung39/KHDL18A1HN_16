tham_nien = int(input("nhap tham nien cong tac cua nhan vien: "))
Luong_co_ban = 1350000
if tham_nien < 12:
    he_so = 2.34
elif 12 <= tham_nien < 36:
    he_so = 3.33
elif 36 <= tham_nien < 60:
    he_so = 3.66
else:
    he_so = 3.99
Luong = Luong_co_ban * he_so
print('luong cua nhan vien la:', Luong)