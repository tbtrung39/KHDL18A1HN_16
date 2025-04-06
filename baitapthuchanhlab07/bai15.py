list1_str = input("Nhập danh sách list1 (các số cách nhau bởi dấu cách): ")
list2_str = input("Nhập danh sách list2 (các tên cách nhau bởi dấu cách): ")
list1 = list1_str.split()
list2 = list2_str.split()
if len(list1) == len(list2):
    combined_dict= {}
    for i in range(len(list1)):
        combined_dict[list1[i]] = list2[i]
    print(combined_dict)
else:
    print("Hai danh sách phải có cùng số lượng phần tử.")