n = int(input("Nhập số lượng sinh viên: "))
print("Nhập danh sách sinh viên học C++ (cách nhau bởi khoảng trắng):")
cpp = set(map(int, input().split()))
print("Nhập danh sách sinh viên học Java (cách nhau bởi khoảng trắng):")
java = set(map(int, input().split()))
print("Nhập danh sách sinh viên học Python (cách nhau bởi khoảng trắng):")
python = set(map(int, input().split()))

dem = {}

for i in cpp:
    if i not in dem:
        dem[i] = 1
    else:
        dem[i] += 1

for i in java:
    if i not in dem:
        dem[i] = 1
    else:
        dem[i] += 1

for i in python:
    if i not in dem:
        dem[i] = 1
    else:
        dem[i] += 1

chi_mot = []
hai_ngon_ngu = []
ba_ngon_ngu = []

for i in range(1, n+1):
    if i in dem:
        if dem[i] == 1:
            chi_mot.append(i)
        elif dem[i] == 2:
            hai_ngon_ngu.append(i)
        elif dem[i] == 3:
            ba_ngon_ngu.append(i)

print("Sinh viên chỉ học 1 ngôn ngữ lập trình:")
print(sorted(chi_mot))
print("Sinh viên học 2 ngôn ngữ lập trình:")
print(sorted(hai_ngon_ngu))
print("Sinh viên học cả 3 ngôn ngữ lập trình:")
print(sorted(ba_ngon_ngu))
