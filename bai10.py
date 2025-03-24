st1 = input("Nhap chuoi 1: ")
st2 = input("Nhap chuoi 2: ")
max_sub = ""
for i in range(len(st1)):
    for j in range(i + 1, len(st1) + 1):
        sub = st1[i:j]
        if sub in st2 and len(sub) > len(max_sub):
            max_sub = sub
print("Chuoi con chung dai nhat:", max_sub)