def kiem_tra_chuoi(chuoi):
    if not chuoi:
        return "Lỗi nhập liệu!!! Vui lòng nhập một chuỗi ký tự."
    cac_so = chuoi.split()
    if len(cac_so) == 3:
        try:
            a = float(cac_so[0])
            b = float(cac_so[1])
            c = float(cac_so[2])
            if a <= 0 or b <= 0 or c <= 0:
                return "Lỗi nhập liệu!!! Độ dài các cạnh phải là số dương."
            if not (a + b > c and a + c > b and b + c > a):
                return "Lỗi nhập liệu!!! Ba số này không tạo thành độ dài ba cạnh của một tam giác."
        except ValueError:
            return "Lỗi nhập liệu!!! Vui lòng nhập ba số cách nhau bởi dấu cách."
        return None 
    if "Lỗi ký tự!!!" in chuoi or "Lỗi nhập liệu!!!" in chuoi or "Lỗi nhập lại!!!" in chuoi or "Lỗi nhập trùng lặp!!!" in chuoi:
        return "Lỗi nhập liệu!!! Chuỗi chứa các cụm từ không được phép."
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i+1]:
            return "Lỗi nhập liệu!!! Chuỗi chứa 2 ký tự liền giống nhau."
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]:
            return "Lỗi nhập liệu!!! Chuỗi chứa 4 ký tự liền giống nhau."
    cac_tu = chuoi.split()
    for i in range(len(cac_tu) - 4):
        if cac_tu[i] == cac_tu[i+1] == cac_tu[i+2] == cac_tu[i+3] == cac_tu[i+4]:
            return "Lỗi nhập liệu!!! Chuỗi chứa 5 từ liền giống nhau."
    return None 
while True:
    input_string = input("Vui lòng nhập chuỗi: ")
    loi = kiem_tra_chuoi(input_string)
    if loi:
        print(loi)
    else:
        print("Chuỗi hợp lệ.")
        break 