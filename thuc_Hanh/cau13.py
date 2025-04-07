s = input("Nhập chuỗi: ")
d = {}
for i in range(len(s) - 1):
    k = s[i:i+2]
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
print(d)
