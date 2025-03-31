n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# a. Tạo ra một danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách ban đầu.
B = [so for so in A if so % 3 == 0 and so % 5 != 0]
print("Danh sách B:", B)

# b. Tạo một danh sách C với các phần tử là bình phương của danh sách A.
C = [so**2 for so in A]
print("Danh sách C:", C)

# c. Tạo ra danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3.
import random
D = [random.choice(A) for _ in range(n) if random.choice(A) % 3 == 0]
print("Danh sách D:", D)