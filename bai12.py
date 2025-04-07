# Bài 12: Tạo dictionary từ số nguyên nhập vào

s = input("Nhập số nguyên dương (nhiều chữ số): ")

d = {}
i = 0
while i < len(s) - 1:
    k = int(s[i])
    v = int(s[i+1])
    d[(k, v)] = k * 10 + v
    i += 2

print("Dictionary (i, j) -> 2 chữ số liền kề:")
for key in d:
    print(key, ":", d[key])
