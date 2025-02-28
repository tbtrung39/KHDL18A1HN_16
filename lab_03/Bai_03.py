# Bài 3: Kiểm tra số nguyên tố
n = int(input("Nhập n: "))
i = 2
là_snt = True
while i * i <= n:
    if n % i == 0:
        là_snt = False
        break
    i = i + 1
if là_snt and n > 1:
    print(n, "là số nguyên tố")
else:
    snt_gần_nhất = n
    while True:
        snt_gần_nhất = snt_gần_nhất + 1
        j = 2
        là_snt = True
        while j * j <= snt_gần_nhất:
            if snt_gần_nhất % j == 0:
                là_snt = False
                break
            j = j + 1
        if là_snt:
            print("Số nguyên tố gần nhất:", snt_gần_nhất)
            break