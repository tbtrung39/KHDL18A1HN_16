lich_su_nhap = []
while True:
    try:
        chuoi = input("Nhập chuỗi: ")
        if not chuoi.isalpha():
            raise ValueError("Lỗi ký tự !!!")
        for i in range(len(chuoi) - 1):
            if chuoi[i] == chuoi[i + 1]:
                raise ValueError("Lỗi nhập liệu !!!")
        for i in range(len(chuoi) - 3):
            if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
                raise ValueError("Lỗi nhập lặp lại !!!")
        lich_su_nhap.append(chuoi)
        if len(lich_su_nhap) >= 5:
            if (lich_su_nhap[-1] == lich_su_nhap[-2] == 
                lich_su_nhap[-3] == lich_su_nhap[-4] == 
                lich_su_nhap[-5]):
                raise ValueError("Lỗi nhập trùng lặp!!!")
        print("Chuỗi hợp lệ.")
    except ValueError as e:
        print(e)