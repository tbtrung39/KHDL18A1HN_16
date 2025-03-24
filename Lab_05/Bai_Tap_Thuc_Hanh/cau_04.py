s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
result = ""
len1, len2 = len(s1), len(s2)
i, j = 0, 0
while i < len1 or j < len2:
    if i < len1:
        result += s1[i]
        i += 1
    if j < len2:
        result += s2[j]
        j += 1
print("Chuỗi trộn:", result)