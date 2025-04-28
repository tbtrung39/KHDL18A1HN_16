
def dao_nguoc_so(n, reversed_num=0):
    if n == 0:
        return reversed_num
    reversed_num = reversed_num * 10 + n % 10
    return dao_nguoc_so(n // 10, reversed_num)
n = int(input("Nhập một số tự nhiên: "))
result = dao_nguoc_so(n)
print("Số đảo ngược là:", result)
