def tim_nghiem(n, tong_con_lai, nghiem_hien_tai):
    if n == 0:
        if tong_con_lai == 0:
            print(nghiem_hien_tai)
        return
    for i in range(1, tong_con_lai - n + 2):
        tim_nghiem(n - 1, tong_con_lai - i, nghiem_hien_tai + [i])
def main():
    N = int(input("Nhập tổng N: "))
    n = int(input("Nhập số lượng phần tử n: "))
    print(f"Tất cả các bộ nghiệm x1 + x2 + ... + x{n} = {N}:")
    tim_nghiem(n, N, [])

main()
