# Câu 11
#Cach1:
str = "11111111111101100000000000000001"
decimal = 0
for i in range(len(str)):
    decimal += int(str[i]) * (2 ** (len(str) - i - 1))
print("Số thập phân tương ứng là:", decimal)
#Cach2:
str = "11111111111101100000000000000001"
decimal = int(str, 2)
print("Số thập phân tương ứng là:", decimal)