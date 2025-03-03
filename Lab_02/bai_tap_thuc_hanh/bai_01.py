thang = int(input("Nhập vào tháng: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
elif thang == 2:
    so_ngay = 28
else:
    so_ngay = "Tháng không hợp lệ"
print(f"Tháng {thang} có {so_ngay} ngày.")