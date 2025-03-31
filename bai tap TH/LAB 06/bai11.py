import random  
# Nhập danh sách A  
n = int(input("Nhập số phần tử của danh sách: "))  
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]  
print("Danh sách A:", A)

# Danh sách B: Các phần tử chia hết cho 3 nhưng không chia hết cho 5  
B = [x for x in A if x % 3 == 0 and x % 5 != 0]  
print("Danh sách B:", B)

# Danh sách C: Bình phương các phần tử củacủa A  
C = [x**2 for x in A]  
print("Danh sách C:", C)

# Danh sách D: Lấy ngẫu nhiên các phần tử của AA chia hết cho 3
D = random.sample([x for x in A if x % 3 == 0], k=min(len([x for x in A if x % 3 == 0]), n))  
print("Danh sách D:", D)