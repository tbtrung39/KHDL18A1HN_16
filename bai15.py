# Bài 15: Ghép list tên với list mã thành từ điển

list1 = ['a0', 'a1', 'a2']
list2 = ['ten0', 'ten1', 'ten2']

d = {}

i = 0
while i < 3:
    d[list1[i]] = list2[i]
    i += 1

print("Từ điển tên:")
for k in d:
    print("<" + k + ">:<" + d[k] + ">")
