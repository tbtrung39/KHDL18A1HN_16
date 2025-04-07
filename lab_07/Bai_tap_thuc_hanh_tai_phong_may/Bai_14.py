# Khởi tạo từ điển rỗng
nhi_phan = {}

# Duyệt từ 1 đến 100
for i in range(1, 101):
    # Tính nhị phân thủ công (không dùng hàm bin())
    so = i
    chuoi = ""
    while so > 0:
        du = so % 2
        chuoi = str(du) + chuoi
        so = so // 2
    nhi_phan[i] = chuoi

# In kết quả
print(nhi_phan)