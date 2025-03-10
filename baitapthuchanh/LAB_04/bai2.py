N = int(input('Nhập N: '))
while N < 0:
    N = int(input('Vui lòng nhập lại một số nguyên dương: '))
#PHẦN a
Sa = 0
i = 1
dau = 1
while i <= N:
    Sa += dau * (1 / i)
    dau *= -1
    i += 1
print('Sa =', Sa)
#PHẦN b
Sb = 0
i = 1
while i <= N:
    Sb += 1 / (i*(i + 1))
    i += 1
print('Sb =', Sb)
#PHẦN c
Sc = 0
i = 2
while i <= N:
    Sc += 1 / (i**0.5)
    i += 1
print('Sc =', Sc)