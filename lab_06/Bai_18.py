# Nhập kích thước ma trận
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

# Nhập ma trận A từ bàn phím
A = []
print("Nhập các phần tử của ma trận A:")
for i in range(m):
    row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    while len(row) != n:  # Đảm bảo số phần tử đúng số cột
        print(f"Hãy nhập đúng {n} phần tử!")
        row = list(map(int, input(f"Nhập hàng {i+1} lại: ").split()))
    A.append(row)

# In ma trận A
print("\nMa trận A:")
for row in A:
    print(row)

# Tính tổng các phần tử của ma trận
sum_A = sum(sum(row) for row in A)

# In tổng các phần tử
print("\nTổng các phần tử của ma trận A:", sum_A)