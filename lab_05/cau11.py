s = input("Nhập chuỗi nhị phân: ")
decimal = 0
for i in range(len(s)):
    decimal += int(s[i]) * (2 ** (len(s) - 1 - i))
print("Giá trị thập phân:", decimal)