list1 = input("Nhập danh sách số, cách nhau bằng dấu cách: ").split()
list2 = input("Nhập danh sách tên, cách nhau bằng dấu cách: ").split()

d = {}
for i in range(len(list1)):
    d[int(list1[i])] = list2[i]

print(d)
