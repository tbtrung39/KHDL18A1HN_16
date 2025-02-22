tnct=int(input("Nhập thêm niên công tác của nhân viên"))
if tnct>0 and tnct<12:
    hs=2.34
elif 12<=tnct<36:
    hs=3.33
elif 36<=tnct<60:
    hs=3.66
elif tnct>=60:
    hs=3.99
else:
    print("Không hợp lệ, vui lòng nhập lại")

print("Lương của nhân viên là: ",hs*1350000)