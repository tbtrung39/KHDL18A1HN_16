tnct = int(input("Nhập thâm niên công tác của nhân viên:"))
luong_co_ban = 1350000
luong = 0
if tnct < 12 :
    luong = luong_co_ban*2.34
    print(f"Lương thực tế là: {luong}")
elif 12 <= tnct <= 36:
    luong = luong_co_ban*3.33
    print(f"Lương thực tế là: {luong}")
elif 36 <= tnct <= 60:
    luong = luong_co_ban*3.66
    print(f"Lương thực tế là: {luong}")
else: 
    luong = luong_co_ban*3.99
    print(f"Lương thực tế là: {luong}")
