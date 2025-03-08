so = int(input("Nhập một số: "))
tong = 0
while so > 0:
    chu_so = so % 10  
    tong = tong + chu_so  
    so = so // 10  
print("Tổng các chữ số là:", tong)
