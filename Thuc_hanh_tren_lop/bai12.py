balance = 0
n = int(input("Nhập số lượng giao dịch: "))
for _ in range(n):
    transaction = input("Nhập giao dịch (D/W số tiền): ").split()
    if len(transaction) != 2:
        print("Giao dịch không hợp lệ, vui lòng nhập lại.")
        continue  
    action = transaction[0]
    try:
        amount = int(transaction[1])
    except ValueError:
        print("Số tiền không hợp lệ, vui lòng nhập lại.")
        continue 
    if action == 'D':
        balance += amount  
    elif action == 'W':
        balance -= amount 
    else:
        print("Loại giao dịch không hợp lệ, vui lòng nhập lại.")
        continue  
print(f"Số tiền thực của tài khoản là: {balance}")
