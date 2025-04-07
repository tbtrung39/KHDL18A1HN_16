# Bài 11: Danh sách sinh viên Olympic theo C++, Java, Python

ds_sinh_vien = {
    "C++": ["h1", "h2", "h3"],
    "Java": ["h2", "h4", "h5"],
    "Python": ["h1", "h5", "h6"]
}

# a. Sinh viên chỉ thi 1 ngôn ngữ
dem = {}

for ngon_ngu in ds_sinh_vien:
    for sv in ds_sinh_vien[ngon_ngu]:
        if sv in dem:
            dem[sv] += 1
        else:
            dem[sv] = 1

chi_1 = []
tren_1 = []
ca_3 = []

for sv in dem:
    if dem[sv] == 1:
        chi_1.append(sv)
    if dem[sv] > 1:
        tren_1.append(sv)
    if sv in ds_sinh_vien["C++"] and sv in ds_sinh_vien["Java"] and sv in ds_sinh_vien["Python"]:
        ca_3.append(sv)

print("Sinh viên thi đúng 1 ngôn ngữ:", chi_1)
print("Sinh viên thi trên 1 ngôn ngữ:", tren_1)
print("Sinh viên thi cả 3 ngôn ngữ:", ca_3)
