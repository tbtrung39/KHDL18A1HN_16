# Bài 4: In số nguyên tố nhỏ hơn hoặc bằng n
n = int(input("Nhập n: "))
x = 2
while x <= n:
    i = 2
    là_snt = True
    while i * i <= x:
        if x % i == 0:
            là_snt = False
            break
        i = i + 1
    if là_snt:
        print(x, end=" ")
    x = x + 1
print()