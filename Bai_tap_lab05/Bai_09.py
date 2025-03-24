chuoi = input("Nhập chuỗi: ")
if len(chuoi) == 0:
    print("Chuỗi rỗng")
else:
    max_char = chuoi[0]
    current = chuoi[0]
    max_len = 1
    current_len = 1
    
    for i in range(1, len(chuoi)):
        if chuoi[i] == chuoi[i-1]:
            current_len = current_len + 1
            if current_len > max_len:
                max_len = current_len
                max_char = chuoi[i]
        else:
            current_len = 1
    print("Chuỗi con dài nhất:", max_char * max_len)