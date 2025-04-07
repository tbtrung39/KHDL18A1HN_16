a = [1, 2, 3, 2, 4]
count = 0
n = len(a)
pairs = []

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            count += 1
            pairs.append((i + 1, j + 1))  # +1 để chuyển từ index 0-based sang 1-based

print("Số cặp chỉ số:", count)
print("Các cặp chỉ số:", pairs)