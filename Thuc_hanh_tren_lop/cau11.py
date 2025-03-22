#c1
binary_str = input("Nhập chuỗi nhị phân: ")
decimal = 0
for bit in binary_str:
    decimal = decimal * 2 + int(bit)
print("số thập phân tương ứng: ",decimal)

##c2
binary_str = input("Nhập chuỗi nhị phân: ")
decimal = 0
length = len(binary_str)
for i in range(length):
    bit = int(binary_str[i])
    decimal += bit * (2 ** (length - 1 -i))
print("số thập phân tương ứng: ",decimal)

