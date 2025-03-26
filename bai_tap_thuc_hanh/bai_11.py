import random
n = int(input("Nhập số phần tử của danh sách:"))
A = [int(input(f"Nhập phần tử thứ {i +1}:")) for i in range(n)]
B = [ x for x in A if x % 3 == 0 and x % 5 != 0]
C = [ x**2 for x in A]
D = random.sample([ x for x in A if x % 3 == 0], min(len([x for x in A if x % 3 == 0]),n))
print("\n Danh sách A :",A)
print("Danh sách B (chia hết cho 3 nhưng ko chia hết cho 5):",B)
print("Danh sách C (bình phương cảu A):",C)
print("Danh sách D(số ngẫu nhiên từ A chia hết cho 3):",D)