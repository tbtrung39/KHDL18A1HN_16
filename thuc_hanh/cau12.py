transactions = []
while True:
    data = input("Nhập giao dịch (D/W số tiền), nhập 'exit' để kết thúc: ")
    if data.lower() == 'exit':
        break
    transactions.append(data)

balance = 0
for transaction in transactions:
    action, amount = transaction.split()
    amount = int(amount)
    if action == "D":
        balance += amount
    elif action == "W":
        balance -= amount

print("Số dư tài khoản:", balance)
