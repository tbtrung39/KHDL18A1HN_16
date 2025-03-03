N = int(input("Nhập N: "))
print("Các số nguyên tố bé hơn hoặc bằng", N, "là:")
for i in range(2, N + 1):
    nguyen_to = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            nguyen_to = False
            break
    if nguyen_to:
        print(i)