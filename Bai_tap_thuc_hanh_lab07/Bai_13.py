s = input("Nhập chuỗi: ")
d = {}

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        k = s[i:j]
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

print(d)
