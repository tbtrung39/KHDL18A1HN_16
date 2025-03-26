n = int(input("Nhập phần tử của danh sách:"))
arr = list(map(int,input("Nhập danh sách các số tự nhiên:").split()))
if n < 2:
    print("Danh sách phải có ít nhất 2 phàn tử")
else:
    max1=max2=float('-int')
    for num in arr:
        if num > max1:
            max2 = max1
            max1=num
        elif max2< num < max1:
            max2 = num 
    if max2 == float('-int'):
        print("không có phần tử lớn hơn 2")
    else:
        positions = [i for i in range(n) if arr[i] == max2]
        print(f'Phần tử lớn thứ 2:{max2}')
        print(f'vị trí cảu phần tử lớn thứ 2: {positions}')
max_lenghth = 0
current_lenghth= 0
for num in arr:
    if num > 0:
        current_lenghth +=1
        max_lenghth = max(max_lenghth,current_lenghth)
    else:
        current_lenghth = 0
print(f'Số lương số dương liên tiếp dài nhất:{max_lenghth}')
max_sum = 0
current_sum = 0
max_count= 0
curent_count=0
for num in arr:
    if num > 0:
        current_sum += num
        curent_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_count = curent_count
    else:
        current_sum = 0
        curent_count = 0
print(f'Số lượng số dương liên tiếp có tổng lớn nhất :{max_count}')