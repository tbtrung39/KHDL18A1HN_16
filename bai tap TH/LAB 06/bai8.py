n = int(input("Nhập số phần tử của dãy Fibonacci: "))
day_fib = [0, 1]
for i in range(2, n):
    day_fib.append(day_fib[i - 1] + day_fib[i - 2])
print("Dãy Fibonacci:", ",".join(map(str, day_fib[:n])))