def kt_so_max(x, y, z):
    max = x
    if max < y :
        max = y
    if max < z:
        max = z
    return max
def kt_so_min(x, y, z):
    min = x
    if min > y:
        min = y
    if min > z:
        min = z
    return min
x, y, z = map(int,input("Nhập x, y, z: ").split(" "))
print(f"Số max: {kt_so_max(x, y, z)}")
print(f"Số min: {kt_so_min(x, y, z)}")