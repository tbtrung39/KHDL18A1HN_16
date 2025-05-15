def in_uoc_so(N):
    print(f"Các ước số của {N} là:")
    for i in range(1, N + 1):
        if N % i == 0:
            print(i, end=' ')

N = int(input("Nhập số nguyên dương N: "))

if N <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    in_uoc_so(N)
