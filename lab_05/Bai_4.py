# Nhập chuỗi từ bàn phím
Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")

# Cách 1: Dùng công thức với zip
merged1 = "".join("".join(pair) for pair in zip(Str1, Str2)) + Str1[len(Str2):] + Str2[len(Str1):]
print("Chuỗi trộn (cách 1):", merged1)

# Cách 2: Dùng vòng lặp
merged2 = ""
i = 0
length1 = len(Str1)
length2 = len(Str2)

while i < length1 or i < length2:
    if i < length1:
        merged2 += Str1[i]
    if i < length2:
        merged2 += Str2[i]
    i += 1

print("Chuỗi trộn (cách 2):", merged2)