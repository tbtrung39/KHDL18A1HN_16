def x_n(n, memo=None):
    # Khởi tạo dictionary lưu trữ các giá trị đã tính
    if memo is None:
        memo = {0: 1}  # X0 = 1
    
    # Nếu X_n đã được tính trước, trả về giá trị đã lưu
    if n in memo:
        return memo[n]
    
    # Tính giá trị X_n theo công thức truy hồi
    result = sum((i**2) * x_n(i, memo) for i in range(n))
    
    # Lưu kết quả vào memo để tránh tính lại
    memo[n] = result
    return result

# Nhập giá trị n
n = int(input("Nhập giá trị n: "))
print(f"Giá trị của X_{n} là: {x_n(n)}")