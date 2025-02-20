num = int(input("Nhập số nguyên: "))
if num >= 100 or num <= -100:
    num1 = abs(num) // 100
    print(f"Chữ số hàng trăm của {num} là: {num1}")
else:
    print(0)