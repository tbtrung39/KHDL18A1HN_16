n = int(input("Nhập số phần tử n: "))
lst = []
i = 0
while i < n:
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    lst.append(x)
    i = i + 1

# Tìm phần tử lớn thứ hai và vị trí
max1 = -1
max2 = -1
pos = -1
i = 0
while i < n:
    if lst[i] > max1:
        max2 = max1
        max1 = lst[i]
    elif lst[i] > max2 and lst[i] != max1:
        max2 = lst[i]
        pos = i
    i = i + 1
print("Phần tử lớn thứ hai là:", max2, ", tại vị trí:", pos)

# Tính số lượng số dương liên tiếp nhiều nhất
count = 0
max_count = 0
i = 0
while i < n:
    if lst[i] > 0:
        count = count + 1
        if count > max_count:
            max_count = count
    else:
        count = 0
    i = i + 1
print("Số lượng số dương liên tiếp nhiều nhất:", max_count)

#  Tính tổng các số dương liên tiếp có tổng lớn nhất
tong = 0
tong_max = 0
i = 0
while i < n:
    if lst[i] > 0:
        tong = tong + lst[i]
        if tong > tong_max:
            tong_max = tong
    else:
        tong = 0
    i = i + 1
print("Tổng lớn nhất của các số dương liên tiếp:", tong_max)
