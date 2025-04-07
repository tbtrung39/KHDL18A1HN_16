# Bài 13: Tạo dictionary từ chuỗi ký tự

chuoi = input("Nhập chuỗi ký tự: ")

d = {}
i = 0
while i < len(chuoi) - 1:
    k = chuoi[i]
    v = chuoi[i+1]
    d[(k, v)] = k + v
    i += 1

print("Dictionary chứa các cặp ký tự liên tiếp:")
for key in d:
    print(key, ":", d[key])
