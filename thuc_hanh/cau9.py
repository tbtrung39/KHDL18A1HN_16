
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

so_nguyen_to_count = 0
for num in a:
    if num > 1: 
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            so_nguyen_to_count += 1
print("Số lượng số nguyên tố trong danh sách là:", so_nguyen_to_count)
