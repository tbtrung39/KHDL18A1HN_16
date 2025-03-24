chuoi = input("nhap chuoi:")
kq = ""
for c in chuoi:
    if '0' <= c <= '9':
        kq += c
print("Chuoi chi gom so:", kq)