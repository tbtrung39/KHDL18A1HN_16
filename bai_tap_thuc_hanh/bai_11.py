def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return (n - 2) * double_factorial(n - 2)

n = int(input("Nhập n để tính n!!: "))
print(f"{n}!! =", double_factorial(n))







def total_sum(k):
    if k == 0:
        return 0
    return ((-1)**k) * double_factorial(k) + total_sum(k-1)

k = int(input("Nhập k (<1000): "))
print("Tổng S =", total_sum(k))