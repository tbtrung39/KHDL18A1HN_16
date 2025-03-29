m, n = map(int, input("Nhập số lượng hàng và cột của ma trận (m n): ").split())
A = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = list(map(int, input(f"Nhập các phần tử của hàng {i+1}: ").split()))
    A.append(row)
total_sum = sum(sum(row) for row in A)
print("Ma trận A là:")
for row in A:
    print(row)
print(f"Tổng các phần tử của ma trận A là: {total_sum}")
