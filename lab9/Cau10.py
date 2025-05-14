# Câu 10 
def tinh_X(n, X_cache=None):
    if X_cache is None:
        X_cache = {0: 1}  
    if n in X_cache:
        return X_cache[n]
    X_n = sum((i ** 2) * tinh_X(i, X_cache) for i in range(n))
    X_cache[n] = X_n
    return X_n
n = int(input("Nhập giá trị n: "))
Xn = tinh_X(n)
print(f"Giá trị của X_{n} là: {Xn}")