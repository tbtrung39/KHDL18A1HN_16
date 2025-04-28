
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def ucln_list(arr, n):
    if n == 1:
        return arr[0]
    else:
        return ucln(arr[n - 1], ucln_list(arr, n - 1))
n = int(input("Nhập số lượng số nguyên: "))
arr = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    arr.append(num)
ket_qua = ucln_list(arr, n)
print("Ước chung lớn nhất là:", ket_qua)
