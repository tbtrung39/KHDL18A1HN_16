A = input("Nhập A: ")
B = input("Nhập B: ")
exp = ""
for i in range(min(len(A), len(B))):
    exp += A[i] + '+' + B[i]
exp = exp.rstrip('+')
try:
    result = eval(exp)
    print(exp, "=", result)
except:
    print("Không tồn tại cách đặt!")