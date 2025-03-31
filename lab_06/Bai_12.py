# Khởi tạo số dư tài khoản
balance = 0

while True:
    transaction = input("Nhập giao dịch (D để gửi, W để rút, Enter để kết thúc): ").strip()
    
    if not transaction:  # Nhấn Enter để kết thúc nhập
        break

    try:
        action, amount = transaction.split()  # Tách thành 2 phần: loại giao dịch và số tiền
        amount = int(amount)  # Chuyển số tiền sang kiểu số nguyên

        if action.upper() == 'D':  # Gửi tiền
            balance += amount
        elif action.upper() == 'W':  # Rút tiền
            balance -= amount
        else:
            print("Lệnh không hợp lệ! Vui lòng nhập lại.")
    except ValueError:
        print("Lỗi định dạng! Hãy nhập đúng theo dạng: D 100 hoặc W 200.")

# In số dư tài khoản cuối cùng
print("Số dư tài khoản cuối cùng:", balance)