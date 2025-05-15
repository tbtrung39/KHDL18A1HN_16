def la_nam_nhuan(y):
    """Trả về True nếu y là năm nhuận, ngược lại False"""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay_trong_thang(m, y):
    """Trả về số ngày của tháng m trong năm y"""
    if m < 1 or m > 12:
        return -1 
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if la_nam_nhuan(y) else 28

y = int(input("Nhập năm (y): "))
m = int(input("Nhập tháng (1-12): "))

if la_nam_nhuan(y):
    print(f"Năm {y} là năm nhuận.")
else:
    print(f"Năm {y} không phải là năm nhuận.")

ngay = so_ngay_trong_thang(m, y)
if ngay == -1:
    print("Tháng không hợp lệ.")
else:
    print(f"Tháng {m} năm {y} có {ngay} ngày.")
