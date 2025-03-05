# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Duyệt tất cả các số từ 2 đến n-1
for num in range(2, n):
    tong_uoc = 0  # Biến lưu tổng các ước số thực sự
    
    # Tìm các ước số thực sự của num
    for i in range(1, num):
        if num % i == 0:  # Nếu i là ước số
            tong_uoc += i  # Cộng vào tổng
    
    # Kiểm tra nếu tổng các ước số bằng chính nó
    if tong_uoc == num:
        print(num, end=" ")  # In số hoàn hảo ra màn hình