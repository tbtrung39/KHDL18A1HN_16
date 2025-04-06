n = int(input("Nhập số sinh viên: "))

sv = {}

for i in range(n):
    print("Nhập thông tin sinh viên thứ", i+1)
    ma = input("Mã sinh viên (6 ký tự): ")
    ten = input("Tên sinh viên: ")
    diem = int(input("Điểm số (0 - 100): "))
    sv[ma] = [ten, diem]

ds_sap_xep = sorted(sv.items(), key=lambda x: x[1][1], reverse=True)

print("Danh sách sinh viên theo điểm giảm dần:")
for item in ds_sap_xep:
    print("Mã:", item[0], "| Tên:", item[1][0], "| Điểm:", item[1][1])
