n = int(input("Nhập n: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
if n > 0:
    print("Dãy Fibonacci:", end="")
    for i in range(len(fib)):
        print(fib[i], end="")
        if i < len(fib) - 1:
            print(", ", end="")
    print()  
else:
    print("Dãy Fibonacci:") 