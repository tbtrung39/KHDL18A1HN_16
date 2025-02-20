# 5

def tinh_tich_vo_huong(a, b):
    if any(i >= len(b) for i in range(len(a))) or any(i >= len(a) for i in range(len(b))):
        print("Hai vector phải có cùng số phần tử.")
    else:
        print(f"Tích vô hướng của hai vector là: {sum(x * y for x, y in zip(a, b))}")

# Nhập dữ liệu từ bàn phím
n = int(input("Nhập số phần tử của vector: "))

a = [float(input(f"a[{i}]: ")) for i in range(n)]
b = [float(input(f"b[{i}]: ")) for i in range(n)]

# Gọi hàm mà không cần return
tinh_tich_vo_huong(a, b)