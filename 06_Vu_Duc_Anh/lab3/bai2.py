n = int(input("Nhập n: "))
i = 1

while i < n:
    sum_div = 0
    j = 1
    while j < i:
        if i % j == 0:
            sum_div += j
        j += 1

    if sum_div == i:
        print(i, end=" ")
    i += 1
