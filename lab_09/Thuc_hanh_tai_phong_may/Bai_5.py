# Hàm đệ quy sinh các hoán vị
def permutation(n):
    if n == 1:
        return [[1]]  # Trường hợp cơ bản
    else:
        result = []
        prev = permutation(n - 1)  # Lấy tất cả hoán vị của n-1 phần tử trước
        for p in prev:
            for i in range(len(p) + 1):
                new_p = p[:i] + [n] + p[i:]  # Chèn n vào tất cả vị trí có thể
                result.append(new_p)
        return result

# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Gọi hàm và in kết quả
ds_hoan_vi = permutation(n)
print(f"Tất cả hoán vị của dãy từ 1 đến {n}:")
for hv in ds_hoan_vi:
    print(hv)