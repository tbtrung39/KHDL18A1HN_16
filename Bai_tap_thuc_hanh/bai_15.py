n = int(input("Nhập số lượng phần tử: "))

print("Nhập các phần tử của list1 (cách nhau bởi khoảng trắng):")
list1 = input().split()

print("Nhập các phần tử của list2 (cách nhau bởi khoảng trắng):")
list2 = input().split()

d = {}

for i in range(n):
    khoa = list1[i]
    gia_tri = list2[i]
    d[khoa] = gia_tri

print("Nội dung của từ điển:")
for k in d:
    print(k + ":" + d[k])
