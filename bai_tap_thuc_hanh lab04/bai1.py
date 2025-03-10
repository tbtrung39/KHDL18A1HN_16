N = int(input('Nhập số nguyên dương N: '))
while N <= 0:
    N = int(input('vui lòng nhập lại một số nguyên dương N: '))
#PHẦN a
S4 = 0
i = 1
while i <= N:
    S4 = S4 + i**2
    i += 1
print('S4 =', S4)

#PHẦN b
S5 = 0
i = 1
tong = 0
while tong < N:
    S5 = S5 + i**3
    i += 2
    tong += 1
print('S5 =', S5)

#PHẦN c
S6 = 0
i = 2
tong = 0
while tong < N:
    S6 = S6 + i**4
    i += 2
    tong += 1
print('S6 =', S6)