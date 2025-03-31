# Nhập số phần tử cho danh sách A
n = int(input("Nhập số lượng phần tử cho danh sách A: "))

# Nhập danh sách A
A = []
for _ in range(n):
    A.append(int(input("Nhập một số nguyên: ")))

# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết cho 3 nhưng không chia hết cho 5):", B)

# b. Tạo danh sách C với các phần tử là bình phương của danh sách A
C = [x ** 2 for x in A]
print("Danh sách C (bình phương của các phần tử trong A):", C)

# c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
D = [x for x in A if x % 3 == 0]
print("Danh sách D (các phần tử chia hết cho 3):", D)
