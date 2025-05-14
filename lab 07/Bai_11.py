n = int(input("Nhập số lượng sinh viên: "))

a = int(input("Nhập số sinh viên thi C++: "))
cpp = set(map(int, input("Nhập danh sách sinh viên thi C++: ").split()))

b = int(input("Nhập số sinh viên thi Java: "))
java = set(map(int, input("Nhập danh sách sinh viên thi Java: ").split()))

c = int(input("Nhập số sinh viên thi Python: "))
python = set(map(int, input("Nhập danh sách sinh viên thi Python: ").split()))

count = {}
for sinh_vien in cpp:
    if sinh_vien in count:
        count[sinh_vien] += 1
    else:
        count[sinh_vien] = 1
for sinh_vien in java:
    if sinh_vien in count:
        count[sinh_vien] += 1
    else:
        count[sinh_vien] = 1
for sinh_vien in python:
    if sinh_vien in count:
        count[sinh_vien] += 1
    else:
        count[sinh_vien] = 1

thi_mot_ngon_ngu = []
thi_hai_ngon_ngu = []
thi_ca_ba_ngon_ngu = []
for sinh_vien, so_ngon_ngu in count.items():
    if so_ngon_ngu == 1:
        thi_mot_ngon_ngu.append(sinh_vien)
    elif so_ngon_ngu == 2:
        thi_hai_ngon_ngu.append(sinh_vien)
    elif so_ngon_ngu == 3:
        thi_ca_ba_ngon_ngu.append(sinh_vien)

print("Sinh viên chỉ thi một ngôn ngữ:", sorted(thi_mot_ngon_ngu))
print("Sinh viên thi hai ngôn ngữ:", sorted(thi_hai_ngon_ngu))
print("Sinh viên thi cả ba ngôn ngữ:", sorted(thi_ca_ba_ngon_ngu))