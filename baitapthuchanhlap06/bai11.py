A = []
n = int(input("Nhập số lượng phần tử của danh sách A: "))
for i in range(n):
  x = int(input(f"Nhập phần tử thứ {i+1}: "))
  A.append(x)
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
C = [x**2 for x in A]
D = []
for x in A:
  if x % 3 == 0:
    D.append(x)
print(f"Danh sách B: {B}")
print(f"Danh sách C: {C}")
print(f"Danh sách D: {D}")