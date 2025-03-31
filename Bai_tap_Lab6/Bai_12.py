balance = 0
print("Nhập giao dịch (D/W số tiền), Enter để kết thúc:")
while True:
    transaction = input().strip()
    if not transaction:
        break
    op, amount = transaction.split()
    amount = int(amount)
    if op == 'D':
        balance += amount
    elif op == 'W':
        balance -= amount
print("Số dư cuối cùng:", balance)