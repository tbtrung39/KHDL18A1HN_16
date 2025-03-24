s = input("Nhập chuỗi: ")
numeric = ""
for c in s:
    if '0' <= c <= '9':
        numeric += c
if numeric:
    num = int(numeric)
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    print("Số hoàn hảo" if sum_divisors == num else "Không phải số hoàn hảo")
else:
    print("Không có số hợp lệ trong chuỗi")