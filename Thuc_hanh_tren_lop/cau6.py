number = int(input("Nhập vào một số nguyên có ba chữ số: "))
if number >= 100 and number <= 999 or number <= -100 and number >= -999:
    hundreds = abs(number) // 100  
    tens = (abs(number) % 100) // 10  
    ones = abs(number) % 10  
    ones_list = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
    tens_list = ["", "Mười", "Hai Mươi", "Ba Mươi", "Bốn Mươi", "Năm Mươi", "Sáu Mươi", "Bảy Mươi", "Tám Mươi", "Chín Mươi"]
    if number < 0:
        print("Số bạn nhập là: Âm", end=" ")
    if hundreds > 0:
        print(ones_list[hundreds], "Trăm", end=" ")
    if tens > 0:
        print(tens_list[tens], end=" ")
    if ones > 0:
        print(ones_list[ones])
    else:
        print()
else:
    print("Số nhập vào không hợp lệ. Vui lòng nhập số nguyên có ba chữ số.")