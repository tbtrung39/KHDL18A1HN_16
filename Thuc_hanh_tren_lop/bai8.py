n = int(input("Nhập số phần tử của dãy Fibonacci: "))
fibonacci = [0 if i == 0 else 1 if i == 1 else fibonacci[i-1] + fibonacci[i-2] for i in range(n)]
print(",".join(map(str, fibonacci)))
