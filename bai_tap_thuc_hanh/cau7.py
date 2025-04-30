def tim_nghiem(n, N, nghiem, kq):
    if n == 0:
        if N == 0:
            kq.append(nghiem[:])  # Nếu đúng tổng, lưu bộ nghiệm
        return
    for i in range(N + 1):
        nghiem.append(i)
        tim_nghiem(n-1, N-i, nghiem, kq)
        nghiem.pop()  # Quay lui

# Nhập n và N từ bàn phím
n = int(input("Nhập số lượng biến n: "))
N = int(input("Nhập tổng N: "))

# Danh sách chứa các bộ nghiệm tìm được
kq = []

# Gọi hàm đệ quy tìm nghiệm
tim_nghiem(n, N, [], kq)

# In kết quả
print(f"Tất cả các bộ nghiệm (x1, x2, ..., x{n}) sao cho tổng = {N} là:")
for bo in kq:
    print(bo)