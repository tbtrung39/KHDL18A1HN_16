
with open('lab_11\dayso.dat', 'r') as file:
    data = file.read()
numbers = data.split()
numbers = [int(x) for x in numbers]
tong_le = sum(x for x in numbers if x % 2 == 1)
print("Tổng các số lẻ là:", tong_le)