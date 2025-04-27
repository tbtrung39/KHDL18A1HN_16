def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def ucln_cua_day_so(arr, n):
    if n == 1:
        return arr[0]
    return ucln(arr[n - 1], ucln_cua_day_so(arr, n - 1))

n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    arr.append(x)
    
ket_qua = ucln_cua_day_so(arr, n)
print(f"Ước chung lớn nhất của {n} số là: {ket_qua}")