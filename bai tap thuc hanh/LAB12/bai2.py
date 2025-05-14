def kiem_tra_chuoi(s):
    for c in s:
        if not c.isalpha():
            raise Exception("Lỗi ký tự !!!")

    if len(s) >= 2:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                raise Exception("Lỗi nhập liệu !!!")

    if len(s) >= 4:
        for i in range(len(s)-3):
            if s[i] == s[i+1] == s[i+2] == s[i+3]:
                raise Exception("Lỗi nhập lặp lại !!!")

    if len(s) >= 5:
        for i in range(len(s)-4):
            if len(set(s[i:i+5])) == 1:
                raise Exception("Lỗi nhập trùng lặp!!!")

while True:
    try:
        chuoi = input("Nhập chuỗi ký tự (chỉ chữ cái): ").upper()
        kiem_tra_chuoi(chuoi)
        print("Chuỗi hợp lệ:", chuoi)
        break
    except Exception as e:
        print("Lỗi:", e)