import math
print("Nhập hệ số a, b, c")
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
# Tính delta
delta = b**2 - 4*a*c
# Các trường hơp: 
if a == 0:
    x = -c/b
    print(f"Phương trình có nghiệm: {x:.2f}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print(f"Phương trình có hai nghiệm phan biệt x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b/2*a
        print(f"Phương trình có nghiệm kép: {x}")
    else :
        print("Phương trình bậc 2 vô nghiệm thực")