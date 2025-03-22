n = int(input('Nhập số nguyên dương n:'))
binary=""
if n==0:
    binary ="0"
else:
    while n > 0:
        binary = str(n%2) + binary
        n //=2
print("Số nhị phân tưởng ứng:",binary)