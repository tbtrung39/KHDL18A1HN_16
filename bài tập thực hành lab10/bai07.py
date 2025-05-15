def ktr_so_max(x, y, z):
    max = x
    if max < y :
        max = y
    if max < z:
        max = z
    return max
def ktr_so_min(x, y, z):
    min = x
    if min > y:
        min = y
    if min > z:
        min = z
    return min
x, y, z = map(int,input("Nhập x, y, z: ").split(" "))
print(f"Số max: {ktr_so_max(x, y, z)}")
print(f"Số min: {ktr_so_min(x, y, z)}")