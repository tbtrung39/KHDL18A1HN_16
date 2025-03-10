a = int(input(' nhập số nguyên dương a: '))
b = int(input('Nhập số nguyên dương b: '))
if a <= 0 or b <= 0:
    print('Vui lòng nhập lại 2 số nguyên dương:')
    a = int(input(' nhập số nguyên dương a:'))
    b = int(input('Nhập số nguyên dương b: '))
else:
    if a > b:
        BCNN = a
    else:
        BCNN = b
    while True:
        if BCNN % a == 0 and BCNN % b == 0:
            print('BCNN của', a, 'và', b, 'là:', BCNN)
            break
        BCNN += 1