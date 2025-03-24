van_ban = input("Nhập văn bản: ")
tu = input("Tìm từ: ")
dem = 0
for word in van_ban.split():
    if word == tu:
        dem = dem + 1
print("Xuất hiện", dem, "lần")