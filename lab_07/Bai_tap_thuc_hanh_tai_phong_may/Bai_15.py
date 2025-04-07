# Nhập số phần tử n
n = int(input("Nhập số phần tử: "))

# Nhập list1 gồm n số khác nhau
list1 = []
print("Nhập danh sách số:")
for i in range(n):
    x = int(input())
    list1.append(x)

# Nhập list2 gồm n tên
list2 = []
print("Nhập danh sách tên:")
for i in range(n):
    ten = input()
    list2.append(ten)

# Tạo từ điển từ 2 danh sách
tu_dien = {}

for i in range(n):
    tu_dien[list1[i]] = list2[i]

# In kết quả
print("Từ điển kết quả:")
print(tu_dien)