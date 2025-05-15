def S1(n):
    if n < 1:
        raise ValueError("n phải là số nguyên dương")
    if n == 1:
        return 1
    return n + S1(n - 1)

def S2(n):
    if n < 1:
        raise ValueError("n phải là số nguyên dương")
    if n == 1:
        return 1
    return n**2 + S2(n - 1)

try:
    n = int(input("Nhập số nguyên dương n: "))
    print(f"S1 = {S1(n)}")
    print(f"S2 = {S2(n)}")
except ValueError as e:
    print("Lỗi:", e)