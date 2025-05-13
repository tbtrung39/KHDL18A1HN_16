def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)
def tinh_S2(n):
    if n == 1:
        return 1
    return n * n + tinh_S2(n - 1)
try:
    n_str = input("Nhập n (số nguyên dương): ")
    if not n_str.isdigit():
        raise ValueError("Lỗi: n phải là một số nguyên dương!")
    n = int(n_str)
    if n <= 0:
        raise ValueError("Lỗi: n phải lớn hơn 0!")
    s1 = tinh_S1(n)
    s2 = tinh_S2(n)
    print("S1 = 1 + 2 + ... +", n, "=", s1)
    print("S2 = 1^2 + 2^2 + ... +", n, "^2 =", s2)

except ValueError as e:
    print(e)
except RecursionError:
    print("Lỗi: Quá sâu trong đệ quy! n quá lớn.")
except Exception as e:
    print("Lỗi không xác định:", e)