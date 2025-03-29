import random
A = list(map(int, input("Nhập danh sách A (các số cách nhau bởi dấu cách): ").split()))
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
C = [x ** 2 for x in A]
D = random.sample([x for x in A if x % 3 == 0], k=min(3, len([x for x in A if x % 3 == 0])))
print("Danh sách B:", B)
print("Danh sách C:", C)
print("Danh sách D:", D)
