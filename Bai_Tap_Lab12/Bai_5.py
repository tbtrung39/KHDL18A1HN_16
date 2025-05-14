def S1(n):
    if n == 1:
        return 1
    return n + S1(n - 1)

def S2(n):
    if n == 1:
        return 1
    return n**2 + S2(n - 1)

try:
    n = int(input("Nhập n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương.")
    print(f"S1 = {S1(n)}")
    print(f"S2 = {S2(n)}")
except ValueError as e:
    print("Lỗi:", e)
except RecursionError:
    print("Lỗi: n quá lớn gây tràn bộ nhớ.")