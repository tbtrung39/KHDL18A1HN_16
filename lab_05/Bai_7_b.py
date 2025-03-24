Str = input("Nhập chuỗi ký tự: ")
number_str = ""
for c in Str:
    if '0' <= c <= '9':  # Nếu là ký tự số
        number_str += c

if number_str:  # Nếu chuỗi không rỗng
    number = int(number_str)
    
    # Kiểm tra số hoàn hảo
    sum_divisors = 0
    for i in range(1, number):  # Tính tổng ước số thực sự
        if number % i == 0:
            sum_divisors += i
    
    print("Chuỗi số thu được:", number_str)
    if sum_divisors == number:
        print("Là số hoàn hảo.")
    else:
        print("Không phải số hoàn hảo.")
else:
    print("Không có số trong chuỗi.")