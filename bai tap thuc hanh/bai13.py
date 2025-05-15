def kt_nam_nhuan(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False
def xac_dinh_so_ngay(m,y):
    if m == 1 or\
         m == 3 or\
             m == 5 or\
                 m == 7 or\
                      m == 8 or\
                          m == 10 or\
                              m == 12  :
        print(f"Tháng {m} có 31 ngày")
    elif m == 2:
        if kt_nam_nhuan(y):
            print(f"Tháng {m} có 28 ngày")
        else:
            print(f"Tháng {m} có 29 ngày")
    else:
        print(f"Tháng {m} có 30 ngày")
y = int(input("Nhập năm muốn ktr: "))
m = int(input("Nhập tháng muốn ktr: "))
if kt_nam_nhuan(y):
    print(f"{y} là năm nhuận")
else:
    print(f"{y} là năm không nhuận")
xac_dinh_so_ngay(m,y)