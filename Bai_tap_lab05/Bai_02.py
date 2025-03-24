chuoi = input("Nhập chuỗi: ")
dem = 0
for ky_tu in chuoi:
    la_chu = ('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z')
    la_so = '0' <= ky_tu <= '9'
    if la_chu == False and la_so == False:
        dem = dem + 1
print("Có", dem, "ký tự đặc biệt")