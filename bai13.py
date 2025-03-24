a = input("Nhap chuoi A: ")
b = input("Nhap chuoi B: ")
dang_thuc = ""
if len(a) == len(b):
    for i in range(len(a)):
        if '0' <= a[i] <= '9' and '0' <= b[i] <= '9':
            dang_thuc += a[i] + '+' + b[i]
            if i != len(a) - 1:
                dang_thuc += '+'
        else:
            print("Khong ton tai cach dat!")
            break
    else:
        print("Dang thuc:", dang_thuc)
else:
    print("Khong ton tai cach dat!")

