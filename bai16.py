a = [1, 2, 3, 2, 4]

# Tìm độ dài n (không dùng len)
n = 0
for _ in a:
    n += 1

# Tạo danh sách kết quả
result = []

# Duyệt tất cả các cặp i < j
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] + a[j] == a[i]:
            result.append((i, j))
        j += 1
    i += 1

# In kết quả
for pair in result:
    print(pair)