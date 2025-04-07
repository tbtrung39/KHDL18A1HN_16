
n = int(input("Nhap so tu nhien n: "))
d = 0
s = 2
while d < n:
    kt = True
    i = 2
    while i * i <= s:
        if s % i == 0:
            kt = False
            break
        i += 1
    if kt:
        print(s, end=" ")
        d += 1
    s += 1
