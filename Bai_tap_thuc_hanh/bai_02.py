numbers_input = input("Nhập các số tự nhiên, cách nhau bởi dấu cách: ")
numbers_str = numbers_input.split()
numbers = []
for num_str in numbers_str:
    numbers.append(int(num_str))
a = set()
for num in numbers:
    a.add(num)

print("Danh sách Numbers:", numbers)
print("Set A:", a)