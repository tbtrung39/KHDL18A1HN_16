import random
n = int(input("Nhập số lượng phần tử n: "))
if n <= 0:
    print("n phải là số nguyên dương!")
else:
    A = set()
    while len(A) < n:
        A.add(random.uniform(-100, 100))  
    print("Tập hợp A:", A)
    min_value = min(A)
    print("Phần tử nhỏ nhất:", min_value)
    
    max_value = max(A)
    print("Phần tử lớn nhất:", max_value)
    sum_value = sum(A)
    print("Tổng các phần tử:", sum_value)