n = int(input("Nhập n: "))
count = 0
num = 2
primes = []

while count < n:
    check = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            check = False
            break
    if check:
        primes.append(num)
        count += 1
    num += 1

print("Dãy nguyên tố đầu tiên:", primes)