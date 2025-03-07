num = int(input("Nhập một số: "))
total = 0
while num > 0:
    total += num % 10  
    num //= 10  
print("Tổng các chữ số là:", total)
