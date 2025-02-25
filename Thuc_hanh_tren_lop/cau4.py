number = int(input("Nhập vào một số nguyên: "))
if number >= 100 or number <= -100:
    while abs(number) >= 100: 
        number = number // 10
    print("Chữ số hàng trăm là:", abs(number) // 10)
else:
    print("Chữ số hàng trăm là: 0")