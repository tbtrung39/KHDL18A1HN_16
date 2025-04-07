n = int(input("Nhập số phần tử n: "))
list1 = [int(x) for x in input("Nhập danh sách số: ").split()]
list2 = input("Nhập danh sách tên: ").split()

if len(list1) == n and len(list2) == n:
    result_dict = {list1[i]: list2[i] for i in range(n)}
    print("Dictionary kết quả:", result_dict)
else:
    print("Số lượng phần tử không khớp!")