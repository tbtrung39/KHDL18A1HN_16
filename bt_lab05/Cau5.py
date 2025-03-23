# Câu 5
#Cach1:
str = input("Nhập một chuỗi ký tự: ")
digits = ""
for char in str:
    if char.isdigit():
        digits += char
if digits:
    number = int(digits)
    factors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
    total = sum(factors)
    if total == number and number != 0:
        print("Chuỗi số là số hoàn hảo")
    else:
        print("Chuỗi số không phải là số hoàn hảo")
else:
    print("Chuỗi không chứa số")
#Cach2:
str = input("Nhập một chuỗi ký tự: ")
digits = ''.join(filter(str.isdigit, str))
if digits:
    number = int(digits)
    factors = [i for i in range(1, number // 2 + 1) if number % i == 0]
    if sum(factors) == number and number != 0:
        print("Chuỗi số là số hoàn hảo")
    else:
        print("Chuỗi số không phải là số hoàn hảo")
else:
    print("Chuỗi không chứa số")