def dao_nguoc(n):
    if n == 0:
        return
    print(n % 10, end='')       
    dao_nguoc(n // 10)          

so = int(input("Nhập số nguyên: "))
if so == 0:
    print(0)
else:
    dao_nguoc(so)