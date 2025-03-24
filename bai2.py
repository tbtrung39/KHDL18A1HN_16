chuoi = input("nhap chuoi:")
dem = 0
for c in chuoi:
    if not (('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')):
        dem += 1
print("So ky tu khong phai chu cai va so:", dem)