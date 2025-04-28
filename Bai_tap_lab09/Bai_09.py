def reverse_number(n, reversed_num=0):
    if n == 0:
        return reversed_num
    return reverse_number(n // 10, reversed_num * 10 + n % 10)
num = int(input("Nhập số cần đảo ngược: "))
print("Số đảo ngược:", reverse_number(num))