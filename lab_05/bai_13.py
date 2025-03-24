A = input("Nhap chuoi A: ")
B = input("Nhap chuoi B: ")
kt = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(A[:i] + "+" + A[i:] + "=" + B[:j] + "+" + B[j:])
            kt = True
            break
    if kt:
        break
if not kt:
    print("Không tồn tại cách đặt!")