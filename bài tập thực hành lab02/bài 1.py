thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
if thang==4 or thang==6 or thang==9 or thang==11:
    so_ngay = 30
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay = 29
    else:
        so_ngay = 28
else:
    so_ngay = 31
print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
