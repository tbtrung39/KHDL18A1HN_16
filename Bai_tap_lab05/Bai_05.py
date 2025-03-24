chuoi = input("Nhập chuỗi: ")
so = ""
for c in chuoi:
    if c.isdigit():
        so = so + c
if so == "":
    print("Không có số")
else:
    n = int(so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n and n != 0:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không hoàn hảo")