# Nhập n từ bàn phím
n = int(input("Nhập số phần tử của dãy Fibonacci: "))

# Tạo danh sách Fibonacci bằng list comprehension
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 1)]

# In kết quả, nối các phần tử bằng dấu ","
print(", ".join(map(str, fib)))