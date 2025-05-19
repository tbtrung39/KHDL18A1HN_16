def xu_ly_check_in(input_file='PASSENGERS.IN', 
                   weight_file='WEIGHT.OUT', 
                   canceled_file='CANCELED.OUT'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())  # Số hành khách
    canceled = []
    weights = []

    for idx in range(1, n + 1):
        # Dòng thứ idx chứa trọng lượng các món của hành khách thứ idx
        weights_list = list(map(int, lines[idx].strip().split()))
        total_weight = sum(weights_list)
        item_count = len(weights_list)
        weights.append(total_weight)

        if total_weight > 23 or item_count > 5:
            canceled.append(idx)  # đánh số thứ tự từ 1

    # Ghi tổng trọng lượng vào WEIGHT.OUT
    with open(weight_file, 'w') as wf:
        for w in weights:
            wf.write(str(w) + '\n')

    # Ghi danh sách khách bị hủy vào CANCELED.OUT
    with open(canceled_file, 'w') as cf:
        for c in canceled:
            cf.write(str(c) + '\n')


# Gọi hàm chính
if __name__ == "__main__":
    xu_ly_check_in()