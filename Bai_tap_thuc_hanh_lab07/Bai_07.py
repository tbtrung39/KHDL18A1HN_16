a = input("Nhập ký tự cho A: ")
b = input("Nhập ký tự cho B: ")

A = set()
for ch in a:
    A.add(ch)

B = set()
for ch in b:
    B.add(ch)

common = A & B
print("Phần tử chung:", common)
