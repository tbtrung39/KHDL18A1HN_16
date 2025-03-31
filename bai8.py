n = int(input("Nhập n: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) for i in range(2, n)]
fibonacci_str = ", ".join(map(str, fibonacci))
print(fibonacci_str)