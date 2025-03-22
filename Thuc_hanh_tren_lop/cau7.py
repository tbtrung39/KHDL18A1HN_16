Str = input("Nhập chuỗi Str: ")
result = ""
for char in Str:
    if '0' <= char <= '9':
        result += char
if result == "":
    print("Không có số trong chuỗi.")
else:
    num = int(result)
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    if sum_divisors == num:
        print(f"{num} là số hoàn hảo.")
    else:
        print(f"{num} không phải là số hoàn hảo.")
