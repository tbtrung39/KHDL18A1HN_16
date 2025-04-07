A = {1, 2.5, "hello", 3, "abc", 4.8, 5, "xyz"}

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

print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)
