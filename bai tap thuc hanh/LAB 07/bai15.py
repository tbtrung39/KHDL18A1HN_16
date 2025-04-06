list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D', 'E']
dictionary = {list1[i]: list2[i] for i in range(len(list1))}
print(dictionary)