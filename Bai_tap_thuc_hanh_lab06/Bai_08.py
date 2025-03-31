n = int(input("Nhập vào số n: "))

# Dãy Fibonacci sử dụng list comprehension
fib = [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, n)]
print(",".join(map(str, fib)))
