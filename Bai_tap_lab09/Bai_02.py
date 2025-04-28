def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def find_gcd(numbers):
    if len(numbers) == 2:
        return gcd(numbers[0], numbers[1])
    return gcd(numbers[0], find_gcd(numbers[1:]))
n = int(input("Nhập số lượng số: "))
numbers = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    numbers.append(num)
print("Ước chung lớn nhất là:", find_gcd(numbers))