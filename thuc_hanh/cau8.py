n = int(input("Nhập n: "))
fibo = [0, 1]
[fibo.append(fibo[-1] + fibo[-2]) for _ in range(n-1)]
print("Dãy Fibonacci:", ", ".join(map(str, fibo[:n+1])))
