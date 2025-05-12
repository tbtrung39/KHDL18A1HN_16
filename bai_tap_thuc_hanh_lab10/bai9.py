def phep_cong(a,b):
    return a + b
def phep_tru(a, b):
    return a - b
def phep_nhan(a, b):
    return a*b
def phep_chia(a, b):
    return a/b
a, b = map(int,input("Nhập a, b: ").split(" "))
print(f"Kết quả phép cộng: {phep_cong(a,b)}")
print(f"Kết quả phép trừ: {phep_tru(a,b)}")
print(f"Kết quả phép nhân: {phep_nhan(a,b)}")
print(f"Kết quả phép chia: {phep_chia(a,b):.2f}")