import random
# Nhập danh sách các số nguyên từ bàn phím
n = int(input("Nhập số phần tử n của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(f"Danh sách B (chia hết cho 3 nhưng không chia hết cho 5): {B}")
# b. Tạo danh sách C với các phần tử là bình phương của các phần tử trong danh sách A
C = [x ** 2 for x in A]
print(f"Danh sách C (bình phương của các phần tử trong A): {C}")
# c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ A mà chia hết cho 3
D = [x for x in A if x % 3 == 0]
random.shuffle(D)  
print(f"Danh sách D (các phần tử chia hết cho 3, ngẫu nhiên): {D}")
