
def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return -1

nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))

if la_nam_nhuan(nam):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")

so_ngay = so_ngay_trong_thang(thang, nam)
if so_ngay != -1:
    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
else:
    print("Tháng không hợp lệ.")
