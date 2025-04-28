def tim_nghiem(N, n, index, current, tong):
    if index == n:
        if tong == N:
            print(current)
        return
    for i in range(N - tong + 1): 
        tim_nghiem(N, n, index + 1, current + [i], tong + i)
N = int(input("Nhập giá trị N: "))
n = int(input("Nhập số ẩn n: "))
print(f"Các bộ nghiệm của phương trình x1 + x2 + ... + x{n} = {N} là:")
tim_nghiem(N, n, 0, [], 0)