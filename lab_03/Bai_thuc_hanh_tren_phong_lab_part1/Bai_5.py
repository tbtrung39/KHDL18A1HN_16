# Nhập chiều cao (số dòng) và chiều rộng (số cột)
h = int(input("Nhập chiều cao: "))
w = int(input("Nhập chiều rộng: "))

# Dùng vòng lặp for để vẽ hình chữ nhật
for i in range(h):  # Lặp qua từng dòng
    for j in range(w):  # Lặp qua từng cột trong dòng
        print("*", end="")  # In dấu * mà không xuống dòng
    print()  # Xuống dòng sau mỗi hàng