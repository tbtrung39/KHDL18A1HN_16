n = int(input("Nhập n: "))
fibo = [0, 1]

i = 2
while i < n:
    next_fibo = fibo[i-1] + fibo[i-2]
    fibo.append(next_fibo)
    i = i + 1

# In ra dãy Fibonacci, cách nhau bởi dấu chấm
chuoi = ""
i = 0
while i < len(fibo):
    chuoi = chuoi + str(fibo[i])
    if i != len(fibo) - 1:
        chuoi = chuoi + "."
    i = i + 1

print("Dãy Fibonacci là:", chuoi)
