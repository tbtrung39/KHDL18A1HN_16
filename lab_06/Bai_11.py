import random

# Nhập số phần tử của danh sách
n = int(input("Nhập số phần tử của danh sách A: "))

# Nhập danh sách A từ bàn phím
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("Danh sách A:", A)

# a. Tạo danh sách B: Các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)

# b. Tạo danh sách C: Bình phương các phần tử của A
C = [x**2 for x in A]
print("Danh sách C (bình phương của A):", C)

# c. Tạo danh sách D: Chọn ngẫu nhiên các phần tử trong A mà chia hết cho 3
D = random.sample([x for x in A if x % 3 == 0], min(len([x for x in A if x % 3 == 0]), n))
print("Danh sách D (chọn ngẫu nhiên các số chia hết cho 3 từ A):", D)