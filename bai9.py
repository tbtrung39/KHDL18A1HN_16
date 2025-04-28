def dao_nguoc(n, res=0):
    if n == 0:
        return res
    else:
        return dao_nguoc(n // 10, res * 10 + n % 10)

n = int(input("Nhập số nguyên dương: "))
print("Số đảo ngược là:", dao_nguoc(n))
