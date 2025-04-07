# Khởi tạo số dư ban đầu
balance = 0

# Nhập các giao dịch cho đến khi nhập vào một chuỗi rỗng
while True:
    transaction = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ").strip()
    
    # Dừng nhập khi người dùng nhập một dòng trống
    if transaction == "":
        break
    
    # Tách giao dịch thành hành động và số tiền
    action, amount = transaction.split()
    amount = int(amount)
    
    # Kiểm tra hành động và cập nhật số dư
    if action == "D":
        balance += amount  # Tiền gửi vào
    elif action == "W":
        balance -= amount  # Tiền rút ra

# In số dư cuối cùng
print("Số tiền thực của tài khoản là:", balance)