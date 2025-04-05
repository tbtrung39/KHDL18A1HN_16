n = int(input("Nhập số lượng phần tử của danh sách Numbers: "))
Numbers = []
print("Nhập các số tự nhiên:")
for _ in range(n):
    num = int(input())  
    Numbers.append(num)
A = set(Numbers)

print(f"Tập hợp A: {A}")