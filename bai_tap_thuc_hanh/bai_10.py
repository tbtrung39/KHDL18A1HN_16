memo = {0: 1}  
def tinh_X(n):
    if n in memo:
        return memo[n]
    tong = 0
    for i in range(n):
        he_so = (n - i) ** 2
        tong += he_so * tinh_X(i)    
    memo[n] = tong
    return tong
n = int(input("Nhập n: "))
print(f"Giá trị X{n} là:", tinh_X(n))