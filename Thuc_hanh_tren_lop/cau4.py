Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
result = ""
i = 0
while i < len(Str1) and i < len(Str2):
    result += Str1[i] + Str2[i]
    i += 1
while i < len(Str1):
    result += Str1[i]
    i += 1
while i < len(Str2):
    result += Str2[i]
    i += 1
print("Chuỗi trộn là:", result)
