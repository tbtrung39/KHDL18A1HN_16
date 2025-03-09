thang = int(input("Nhập tháng (1-12): "))

if thang in (1, 3, 5, 7, 8, 10, 12):
    so_ngay = 31
elif thang in (4, 6, 9, 11):
    so_ngay = 30
elif thang == 2:
    nam = int(input("Nhập năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay = 29
    else:
        so_ngay = 28
else:
    print("Tháng không hợp lệ.")
    exit()

print(f"Tháng {thang} có {so_ngay} ngày.")