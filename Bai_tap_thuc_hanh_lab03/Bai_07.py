n = int(input("Nhập n: "))
s = 1
for i in range(2,n+1):
    s += 1/i
print(f"Tổng nghịch đảo của n số nguyên đầu tiên là: {s}")