def ucln(a,b):
    if b == 0 :
        return a
    return ucln(b, a%b)
def ucln_n(numbers , n ):
    if n == 1:
        return numbers[0]
    return ucln(numbers[n - 1] ,ucln_n(numbers(n-1)))

n = int( input("Nhập số :"))
numbers = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}:"))
    numbers.append(num)
ket_qua = ucln_n(numbers, n)
print("Ước chung lớn nhất của các số là:",ket_qua)