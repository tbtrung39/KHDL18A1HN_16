def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

def max_positive_streak(lst):
    max_streak = streak = 0
    for num in lst:
        if num > 0:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    return max_streak

def max_positive_sum(lst):
    max_sum = curr_sum = 0
    for num in lst:
        if num > 0:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        else:
            curr_sum = 0
    return max_sum

numbers = list(map(int, input("Nhập danh sách số tự nhiên: ").split()))
print("Số lớn thứ hai:", second_largest(numbers))
print("Số lượng số dương liên tiếp nhiều nhất:", max_positive_streak(numbers))
print("Tổng lớn nhất của dãy số dương liên tiếp:", max_positive_sum(numbers))
