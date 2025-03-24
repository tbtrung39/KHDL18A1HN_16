van_ban = input("Nhap doan van: ")
dem = 0
for c in van_ban:
    if c == '.' or c == '!' or c == '?':
        dem += 1
print("So cau trong doan van:", dem)
