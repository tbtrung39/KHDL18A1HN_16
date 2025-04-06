n = int(input("Nhập số nguyên n: "))
result_dict = {}
i = 1
while i <= n:
    result_dict[i] = i * i
    i += 1
print(result_dict)