n = int(input("Nhập số lần tung xúc xắc: "))
p_a = 1 / 216
p = 1 - (1 - p_a) ** n
p = round(p, 2)
print("Xác suất ít nhất 1 lần cả 3 ra 6 là:", p)