numbers = input("Nhập các số tự nhiên cách nhau bằng khoảng trắng: ").split()
Numbers = []
for x in numbers:
    Numbers.append(int(x))

A = set()
for x in Numbers:
    A.add(x)

print("Danh sách Numbers:", Numbers)
print("Tập hợp A:", A)
