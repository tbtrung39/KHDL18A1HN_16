def hoan_vi(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]  # hoán đổi
            hoan_vi(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # quay lui

# Nhập số tự nhiên n
n = int(input("Nhập số tự nhiên n: "))

# Tạo dãy từ 1 đến n
day = list(range(1, n + 1))

print(f"Các hoán vị của dãy 1 đến {n} là:")
hoan_vi(day, 0, n - 1)