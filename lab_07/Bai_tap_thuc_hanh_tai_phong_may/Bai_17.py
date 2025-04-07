# Nhập số lượng sinh viên
n = int(input("Nhập số sinh viên: "))

# Khởi tạo từ điển lưu sinh viên
danh_sach = {}

# Nhập thông tin từng sinh viên
for i in range(n):
    print(f"\nNhập thông tin sinh viên thứ {i + 1}:")
    ma = input("Mã sinh viên (6 chữ số): ")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm số: "))
    
    # Làm tròn và giới hạn điểm từ 0 đến 10
    diem = round(diem)
    if diem < 0:
        diem = 0
    elif diem > 10:
        diem = 10

    # Lưu vào từ điển
    danh_sach[ma] = [ten, diem]

# Sắp xếp sinh viên theo điểm giảm dần
# items() -> [(ma, [ten, diem]), ...]
sinh_vien_sap_xep = sorted(danh_sach.items(), key=lambda x: x[1][1], reverse=True)

# In danh sách sau khi sắp xếp
print("\nDanh sách sinh viên theo điểm giảm dần:")
for ma, thong_tin in sinh_vien_sap_xep:
    print(f"Mã: {ma}, Tên: {thong_tin[0]}, Điểm: {thong_tin[1]}")