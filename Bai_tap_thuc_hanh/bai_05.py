Str = input("Nhập chuỗi ký tự: ")
num_str = ""
for c in Str:
    if "0" <= c <= "9":
        num_str += c
if num_str == "":
    print("Không có số nào trong chuỗi.")
else:
    num = int(num_str)
    print("Chuỗi số sau khi lọc:", num)
    sum_divisors = 0  
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print("Số", num, "là số hoàn hảo.")
    else:
        print("Số", num, "không phải là số hoàn hảo.")
