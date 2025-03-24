Str = input("Nhập chuỗi ký tự: ")
number_str = ''.join(c for c in Str if c.isdigit())  # Lọc ra các ký tự số

if number_str:  # Kiểm tra nếu chuỗi không rỗng
    number = int(number_str)  # Chuyển thành số nguyên
    # Kiểm tra số hoàn hảo
    perfect = number > 0 and sum(i for i in range(1, number) if number % i == 0) == number
    print("Chuỗi số thu được:", number_str)
    print("Là số hoàn hảo." if perfect else "Không phải số hoàn hảo.")
else:
    print("Không có số trong chuỗi.")