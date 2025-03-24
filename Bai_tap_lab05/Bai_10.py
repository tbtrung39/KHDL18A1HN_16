str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
max_len = 0
result = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2 and len(sub) > max_len:
            max_len = len(sub)
            result = sub

print("Chuỗi con chung dài nhất:", result)