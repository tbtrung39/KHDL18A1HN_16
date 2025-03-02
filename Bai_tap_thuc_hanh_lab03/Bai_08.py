
n = int(input("Nhập n: "))
if n <= 0:
    print(f"{n} không thỏa mãn vui lòng nhập lại")
# ý a:
s1 = 0
for i in range(1,n+1):
    s1 += i
print(f"Kết quả của biểu thức là: {s1}")
# ý b:
s2 = 0
for j in range(1,n+1,2):
    s2 += j
print(f"Kết quả của biểu thức là: {s2}")
# ý c:
s3 = 0
for k in range(2,n+1,2):
    s3 += k
print(f"Kết quả của biểu thức là: {s3}")