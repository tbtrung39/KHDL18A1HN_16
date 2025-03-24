chuoi = input("Nhap chuoi: ")
dem = 0
for c in chuoi:
    if ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9'):
        dem += 1
print("So ky tu la chu va so:", dem)