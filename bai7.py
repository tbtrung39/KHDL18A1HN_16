chuoi = input("nhap chuoi:")
kq = ""
for c in chuoi:
    if not (('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')):
        kq += c
print("Chuoi sau khi xoa chu cai va so:", kq)
