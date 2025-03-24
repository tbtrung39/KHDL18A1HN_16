chuoi = input("Nhap chuoi: ")
max_len = 0
current_len = 1
max_char = chuoi[0] if chuoi else ''

for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
            max_char = chuoi[i]
    else:
        current_len = 1

print("Chuoi con dai nhat gom cac ky tu giong nhau la:", max_char * max_len)
