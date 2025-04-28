# Hàm đệ quy tính giai thừa kép n!!
def giaithua_kep(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua_kep(n - 2)

# Tính tổng S theo công thức đề bài
def tinh_tong(k):
    S = 0
    for i in range(1, k + 1):
        if (i % 2 == 1):  # i lẻ: dấu cộng
            S += giaithua_kep(i)
        else:  # i chẵn: dấu trừ
            S -= giaithua_kep(i)
    return S

# Nhập k từ bàn phím
k = int(input("Nhập số k (<1000): "))

# Tính và in kết quả
tong_S = tinh_tong(k)
print("Tổng S =", tong_S)