#kiểm tra năm nhuận
print("chuong trinh kiem tra nam nhuan")
nam = int(input("nhap nam can kiem tra: "))
if (nam%4==00 and nam%100 != 0 ) or nam%400 == 0:
    print("nam", nam, "la nam nhuan!")
else:
    print("nam",nam,"khong phai la nam nhuan!")