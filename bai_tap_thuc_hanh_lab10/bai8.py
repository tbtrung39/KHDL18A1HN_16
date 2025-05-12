import math
def C(r):
    return 2*math.pi*r
def S(r):
    return math.pi*r**2
r = int(input("Nhập bán kính: "))
print(f"Chu vi hình tròn: {C(r):.2f}\nDiện tích hình tròn: {S(r):.2f}")