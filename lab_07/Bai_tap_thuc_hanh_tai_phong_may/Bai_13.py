# Nhập chuỗi từ bàn phím
W = input("Nhập chuỗi: ")

# Khởi tạo dictionary rỗng
ket_qua = {}

# Duyệt tất cả các chuỗi con liên tiếp
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        k = W[i:j]
        if k not in ket_qua:
            dem = 0
            for m in range(len(W) - len(k) + 1):
                if W[m:m+len(k)] == k:
                    dem += 1
            ket_qua[k] = dem

# In kết quả
print(ket_qua)