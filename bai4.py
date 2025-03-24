st1 = input("Nhap chuoi 1: ")
st2 = input("Nhap chuoi 2: ")
kq = ""
i = j = 0
while i < len(st1) or j < len(st2):
    if i < len(st1):
        kq += st1[i]
        i += 1
    if j < len(st2):
        kq += st2[j]
        j += 1
print("Chuoi sau khi tron:", kq)