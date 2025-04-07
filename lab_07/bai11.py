# Nhập số lượng sinh viên thi từng ngôn ngữ
a = int(input("Nhập số sinh viên thi C++: "))
b = int(input("Nhập số sinh viên thi Java: "))
c = int(input("Nhập số sinh viên thi Python: "))

# Khởi tạo danh sách lưu số thứ tự sinh viên
cpp = []
java = []
python = []

# Nhập danh sách sinh viên thi C++
print("Nhập danh sách sinh viên thi C++:")
for i in range(a):
    x = int(input())
    cpp.append(x)

# Nhập danh sách sinh viên thi Java
print("Nhập danh sách sinh viên thi Java:")
for i in range(b):
    x = int(input())
    java.append(x)

# Nhập danh sách sinh viên thi Python
print("Nhập danh sách sinh viên thi Python:")
for i in range(c):
    x = int(input())
    python.append(x)

# Gộp toàn bộ sinh viên vào một danh sách
all_students = cpp + java + python

# Đếm số lần xuất hiện
dem = {}

for i in all_students:
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1

# Khởi tạo danh sách kết quả
chi_mot_ngon_ngu = []
hai_ngon_ngu = []
ba_ngon_ngu = []

# Phân loại theo số lần xuất hiện
for i in dem:
    if dem[i] == 1:
        chi_mot_ngon_ngu.append(i)
    elif dem[i] == 2:
        hai_ngon_ngu.append(i)
    elif dem[i] == 3:
        ba_ngon_ngu.append(i)

# Sắp xếp danh sách kết quả để dễ xem
chi_mot_ngon_ngu.sort()
hai_ngon_ngu.sort()
ba_ngon_ngu.sort()

# In kết quả
print("Sinh viên chỉ thi 1 ngôn ngữ:")
print(chi_mot_ngon_ngu)

print("Sinh viên thi 2 ngôn ngữ:")
print(hai_ngon_ngu)

print("Sinh viên thi cả 3 ngôn ngữ:")
print(ba_ngon_ngu)