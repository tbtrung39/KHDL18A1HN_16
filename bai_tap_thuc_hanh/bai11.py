#Cach1:
str = "111111100000000000011110101"
decimal = 0
for i in range(len(str)):
    decimal += int(str[i]) * (2 ** (len(str) - i - 1))
print("So thap phan tuong ung la:", decimal)


#Cach2:
str = "111111100000000000011110101"
decimal = int(str, 2)
print("So thap phan tuong ung la:", decimal)