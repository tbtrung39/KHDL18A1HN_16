def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)
def alternating_sum(k):
    if k == 1:
        return 1
    sign = -1 if k % 2 == 0 else 1
    return sign * double_factorial(k) + alternating_sum(k - 1)
k = int(input("Nhập k (k < 1000): "))
if k >= 1000:
    print("k phải nhỏ hơn 1000")
else:
    print(f"{k}!! =", double_factorial(k))
    print("Tổng đan dấu S =", alternating_sum(k))