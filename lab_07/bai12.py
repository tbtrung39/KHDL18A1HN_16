n = int(input("Nhập số nguyên n: "))
if n < 1:
    print("n phải là số nguyên lớn hơn hoặc bằng 1!")
else:
    squares = {}
    i = 1
    while i <= n:
        squares[i] = i * i
        i += 1
    print("Dictionary:", squares)