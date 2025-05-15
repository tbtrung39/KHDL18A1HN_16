def tim_uoc_so(n):
    uoc_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_list.append(i)
    return uoc_list

# Chương trình chính
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0")
else:
    uoc_so = tim_uoc_so(n)
    print(f"Các ước số của {n} là:", end=" ")
    for uoc in uoc_so:
        print(uoc, end=" ")