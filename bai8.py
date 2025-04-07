# Bài 8: Tạo tập hợp A, đếm số nguyên, số thực, chuỗi

A = set()
n = int(input("Nhập số phần tử: "))
for _ in range(n):
    s = input("Nhập phần tử: ")
    if '.' in s:
        try:
            s = float(s)
        except:
            pass
    else:
        try:
            s = int(s)
        except:
            pass
    A.add(s)

so_nguyen = 0
so_thuc = 0
chuoi = 0

for x in A:
    if type(x) == int:
        so_nguyen += 1
    elif type(x) == float:
        so_thuc += 1
    elif type(x) == str:
        chuoi += 1

print("Số phần tử số nguyên:", so_nguyen)
print("Số phần tử số thực:", so_thuc)
print("Số phần tử chuỗi:", chuoi)
