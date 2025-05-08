def ucln(a,b):
    if b == 0:
        return a
    return ucln(b, a % b)
def ucln_n(lst, n):
    if n == 1:
        return lst[0]
    return ucln(lst[n - 1], ucln_n(lst, n - 1))

n = int(input("Nhập n số để ktr: "))
lst = []
for i in range(n):
    x = int(input("Nhập số ktr: "))
    lst.append(x)
print(ucln_n(lst,n))

