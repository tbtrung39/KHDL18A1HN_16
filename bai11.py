binary = input("Nhap chuoi nhi phan: ")
decimal = 0
for i in range(len(binary)):
    decimal = decimal * 2 + (ord(binary[i]) - ord('0'))
print("So thap phan tuong ung:", decimal)


