a = input("Nhập chuỗi A: ")
b = input("Nhập chuỗi B: ")
tim_thay = False
for i in range(1, len(a)):
    for j in range(1, len(b)):
        c = int(a[:i])
        d = int(a[i:])
        e = int(b[:j])
        f = int(b[j:])
        if c + d == e + f:
            print(a[:i] + "+" + a[i:] + "=" + b[:j] + "+" + b[j:])
            tim_thay = True
            break
    if tim_thay:
        break
if not tim_thay:
    print("Không tồn tại cách đặt!")