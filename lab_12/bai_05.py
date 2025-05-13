def S1(n):
    if n == 1:
        return 1
    return n + S1(n - 1)

def S2(n):
    if n == 1:
        return 1
    return n * n + S2(n - 1)

try:
    n = input("Nhập số nguyên dương n: ")
    if not n.isdigit():
        raise ValueError("Lỗi: n phải là số nguyên dương!")
    n = int(n)
    if n <= 0:
        raise ValueError("Lỗi: n phải lớn hơn 0!")
    s1 = S1(n)
    s2 = S2(n)
    print(f"S1 = {s1}")
    print(f"S2 = {s2}")
except ValueError as v:
    print(v)
except RecursionError:
    print("Lỗi: n quá lớn.")
except Exception as e:
    print("Đã xảy ra lỗi:", e)