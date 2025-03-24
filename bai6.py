chuoi = input("nhap chuoi:")
hex_flag = True
for c in chuoi:
    if not (('0' <= c <= '9') or ('A' <= c <= 'F') or ('a' <= c <= 'f')):
        hex_flag = False
        break
print("La chuoi Hex" if hex_flag else "Khong phai chuoi Hex")