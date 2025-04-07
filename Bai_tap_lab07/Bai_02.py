numbers = []
print("Nhập các số tự nhiên (Enter để kết thúc):")
while True:
    num = input()
    if num == '':
        break
    numbers.append(int(num))
A = set(numbers)
print("Tập hợp A:", A)