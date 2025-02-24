num = int(input("Nhập một số nguyên: "))

if num < 100 and num > -100:
    print("")  # Không xuất gì nếu số không có hàng trăm
else:
    hundreds = (num // 100) % 10
    if hundreds < 0:  
        hundreds = -hundreds  # Đảm bảo chữ số dương
    print("Chữ số hàng trăm là:", hundreds)
