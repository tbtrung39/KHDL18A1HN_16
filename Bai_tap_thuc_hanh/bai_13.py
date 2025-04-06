s = input("Nhập chuỗi: ")

d = {}

for i in range(len(s) - 1):
    k = s[i]
    v = s[i+1]
    cap = k + v

    if cap not in d:
        d[cap] = 1
    else:
        d[cap] += 1

print("Từ điển các cặp ký tự liên tiếp và số lần xuất hiện:")
print(d)
