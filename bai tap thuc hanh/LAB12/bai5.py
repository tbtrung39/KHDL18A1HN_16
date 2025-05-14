def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return n**2 + tong_S2(n - 1)

try:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương!")

    print("Tổng S1 =", tong_S1(n))
    print("Tổng S2 =", tong_S2(n))

except ValueError as e:
    print("Lỗi:", e)