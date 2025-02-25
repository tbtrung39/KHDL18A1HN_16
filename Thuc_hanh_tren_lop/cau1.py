thang = int(input("Nhập tháng (1-12): "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    ngay = 30
elif thang == 2:
    ngay = 28  
else:
    ngay = "Tháng không hợp lệ"
print(f"Tháng {thang} có {ngay} ngày." if isinstance(ngay, int) else ngay)