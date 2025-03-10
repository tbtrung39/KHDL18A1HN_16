n = input("Nhập số: ")

tong = 0

for digit in n:
    if digit.isdigit():  
        tong += int(digit)  

print("Tổng các chữ số là:", tong)
