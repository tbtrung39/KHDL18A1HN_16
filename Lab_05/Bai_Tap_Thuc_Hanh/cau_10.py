s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
dainhatdainhat = ""
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        if s1[i:j] in s2 and len(s1[i:j]) > len(dainhatdainhat):
            dainhatdainhat = s1[i:j]
print("Chuỗi con chung dài nhất:", dainhatdainhat)