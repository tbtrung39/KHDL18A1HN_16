list1 = list(map(int, input("Nhập các số trong list1 (cách nhau bởi dấu cách): ").split()))
list2 = input("Nhập các tên trong list2 (cách nhau bởi dấu cách): ").split()
result_dict = dict(zip(list1, list2))
print(result_dict)