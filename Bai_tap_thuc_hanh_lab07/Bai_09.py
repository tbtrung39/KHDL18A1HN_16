n = int(input("Nhập n: "))

A = set()
for i in range(1, n+1):
    if n % i == 0:
        la_nguyen_to = True
        if i < 2:
            la_nguyen_to = False
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    la_nguyen_to = False
                    break
        if la_nguyen_to:
            A.add(i)

B = set()
for i in range(2, n):
    la_nguyen_to = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to and n % i != 0:
        B.add(i)

print("Tập A:", A)
print("Tập B:", B)
