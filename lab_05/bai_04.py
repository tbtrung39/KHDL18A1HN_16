#Cach1:
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
result = ''.join(a + b for a, b in zip(str1, str2))
result += str1[len(str2):] + str2[len(str1):]
print("Chuỗi sau khi trộn là:", result)


#Cach2:
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
result = ""
min_length = min(len(str1), len(str2))
for i in range(min_length):
    result += str1[i] + str2[i]
result += str1[min_length:] + str2[min_length:]
print("Chuỗi sau khi trộn là:", result)