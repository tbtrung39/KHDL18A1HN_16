n = int(input("Nhập số phần tử n: "))
a = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
if len(a) < 2:
    print("Danh sách có ít hơn 2 phần tử")
else:
    unique_sorted = sorted(list(set(a)), reverse=True)
    if len(unique_sorted) < 2:
        print("Không có phần tử lớn thứ hai")
    else:
        second_max = unique_sorted[1] 
        positions = [i for i, x in enumerate(a) if x == second_max] 
        print("Phần tử lớn thứ hai:", second_max)
        print("Vị trí:", positions)
max_pos_seq = current = 0
for num in a:
    if num > 0:
        current += 1
        max_pos_seq = max(max_pos_seq, current)  
    else:
        current = 0  
print("Số lượng số dương liên tiếp dài nhất:", max_pos_seq)
max_sum = current_sum = current_len = max_len = 0
for num in a:
    if num > 0:
        current_sum += num
        current_len += 1
        if current_sum > max_sum or (current_sum == max_sum and current_len > max_len):
            max_sum = current_sum
            max_len = current_len
    else:
        current_sum = 0
        current_len = 0
print("Số lượng số dương liên tiếp có tổng lớn nhất:", max_len)