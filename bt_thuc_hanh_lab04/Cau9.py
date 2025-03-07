# Câu 9
num = input("Nhập một số nguyên: ")
i = 0
tong = 0

while i < len(num):
    tong += int(num[i])
    i += 1

print("Tổng các chữ số là:", tong)