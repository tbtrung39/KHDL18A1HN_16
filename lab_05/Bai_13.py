# Nhập chuỗi A và B từ bàn phím
A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

found = False  # Biến kiểm tra xem có tìm được cách đặt hay không

# Duyệt tất cả cách đặt dấu '+' trong A
for i in range(1, len(A)):  
    C = int(A[:i])   # Phần trước dấu '+'
    D = int(A[i:])   # Phần sau dấu '+'

    # Duyệt tất cả cách đặt dấu '+' trong B
    for j in range(1, len(B)):  
        E = int(B[:j])  # Phần trước dấu '+'
        F = int(B[j:])  # Phần sau dấu '+'

        # Kiểm tra điều kiện C + D == E + F
        if C + D == E + F:
            print(f"{C} + {D} = {E} + {F}")  
            found = True
            break  # Thoát vòng lặp ngay khi tìm được một kết quả hợp lệ

    if found:
        break  # Thoát vòng lặp ngoài

# Nếu không tìm thấy cách đặt dấu '+'
if not found:
    print("Không tồn tại cách đặt!")