s = input("Nhập chuỗi: ")
num = ""
for c in s:
    if '0' <= c <= '9':
        num += c
if num:
    nu = int(num)
    total = 0
    for i in range(1, nu):
        if nu % i == 0:
            total += i
    print("Số hoàn hảo" if total == nu else "Không phải số hoàn hảo")