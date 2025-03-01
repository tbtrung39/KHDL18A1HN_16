n = int(input("Nhập giá trị n: "))
result = 1.0
term = 1.0
for i in range(1, n):
    term *= (2 * i) / (2 * i + 1)
    result += term
print(round(result, 3))

