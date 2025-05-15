def tinh_s1(n):
    if n == 1:
        return 1 
    return n + tinh_s1(n-1)
def tinh_s2(n):
    if n==1:
        return 1
    return n**2 + tinh_s2(n-1)
try:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        raise ValueError("Giá trị phải là số nguyên dương lớn hơn 0.")
    
    s1 = tinh_s1(n)
    s2 = tinh_s2(n)

    print(f"Tổng S1 = 1 + 2 + ... + {n} = {s1}")
    print(f"Tổng S2 = 1^2 + 2^2 + ... + {n^2} = {s2}")

except ValueError as e:
    print(f"Lỗi: {e}")