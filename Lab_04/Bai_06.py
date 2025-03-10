digit = input("Nhập số n: ")  # Bỏ int() để giữ nguyên dạng chuỗi

if digit.isdigit():  # Kiểm tra xem có phải số hợp lệ không
    for d in digit:  # Lặp qua từng chữ số trong chuỗi
        if d == "0":
            print("Không", end=" ")
        elif d == "1":
            print("Một", end=" ")
        elif d == "2":
            print("Hai", end=" ")
        elif d == "3":
            print("Ba", end=" ")
        elif d == "4":
            print("Bốn", end=" ")
        elif d == "5":
            print("Năm", end=" ")
        elif d == "6":
            print("Sáu", end=" ")
        elif d == "7":
            print("Bảy", end=" ")
        elif d == "8":
            print("Tám", end=" ")
        elif d == "9":
            print("Chín", end=" ")
    print()  # Xuống dòng sau khi in xong
else:
    print("Số không hợp lệ, vui lòng nhập lại!")
