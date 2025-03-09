n = int(input("Nhập số nguyên dương n: "))  
for _ in range(n <= 0):  
    n = int(input("n phải là số nguyên dương. Nhập lại: "))
# Tính các tổng
S1 = 0  
S2 = 0  
S3 = 0  
for i in range(1, n + 1):  
    S1 += i            # S1 = 1 + 2 + ... + n  
    S2 += (2 * i - 1)  # S2 = 1 + 3 + 5 + ... + (2n+1)  
    S3 += (2 * i)      # S3 = 2 + 4 + 6 + ... + 2n  
# In kết quả
print("S1 =", S1, "= (n(n+1))/2 =", (n * (n + 1)) // 2)  
print("S2 =", S2, "= (n+1)^2 =", (n + 1) ** 2)  
print("S3 =", S3, "= n(n+1) =", n * (n + 1))