n = int(input("Nhập n: "))
fib = [0, 1] 
[fib.append(fib[-1] + fib[-2]) for _ in range(2, n+1)]  
fib = fib[:n+1]
print("Dãy Fibonacci:", ", ".join(map(str, fib)))