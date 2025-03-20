s = input("Nhập chuỗi: ")
max_sub, temp = "", ""
for c in s:
    if temp and c != temp[-1]:
        temp = ""
    temp += c
    if len(temp) > len(max_sub):
        max_sub = temp
print("Chuỗi lặp dài nhất:", max_sub)