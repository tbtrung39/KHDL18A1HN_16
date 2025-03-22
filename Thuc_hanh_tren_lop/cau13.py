A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

found = False

# Duyệt qua tất cả các cách chèn dấu '+' vào chuỗi A
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])  # C là phần trước dấu +
        D = int(A[i:])  # D là phần sau dấu +
        E = int(B[:j])  # E là phần trước dấu +
        F = int(B[j:])  # F là phần sau dấu +

        # Kiểm tra nếu biểu thức đúng
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            found = True
            break
    if found:
        break

if not found:
    print("Không tồn tại cách đặt!")
