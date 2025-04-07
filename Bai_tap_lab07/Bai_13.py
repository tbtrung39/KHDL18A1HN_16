w = input("Nhập chuỗi ký tự W: ")
n = len(w)
substring_dict = {}

for i in range(n):
    for j in range(i+1, n+1):
        substring = w[i:j]
        substring_dict[substring] = substring_dict.get(substring, 0) + 1

print("Dictionary chuỗi con:", substring_dict)