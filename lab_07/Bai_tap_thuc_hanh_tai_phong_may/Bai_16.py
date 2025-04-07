# Nhập số phần tử
n = int(input("Nhập số lượng phần tử của dãy: "))

# Nhập dãy số nguyên
a = []
print("Nhập các phần tử của dãy:")
for i in range(n):
    x = int(input())
    a.append(x)

# Tìm các cặp thỏa mãn điều kiện
cap_ket_qua = []

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            cap_ket_qua.append((i + 1, j + 1))  # Đổi về chỉ số bắt đầu từ 1 nếu cần

# In kết quả
print("Các cặp chỉ số (i, j) thỏa mãn a[i] + 1 = a[j]:")
for cap in cap_ket_qua:
    print(cap)