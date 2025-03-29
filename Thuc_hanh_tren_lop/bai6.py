import random
A = [random.randint(1, 99999) for _ in range(1000)]
# 1. Sắp xếp sử dụng hàm sorted()
A_sorted = sorted(A)
print("Danh sách sau khi sắp xếp bằng sorted():")
print(A_sorted)

# 2. 
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
A_copy = A.copy() 
A_sorted_no_sorted = selection_sort(A_copy)
print("Danh sách sau khi sắp xếp bằng thuật toán sắp xếp chọn lựa:")
print(A_sorted_no_sorted)
