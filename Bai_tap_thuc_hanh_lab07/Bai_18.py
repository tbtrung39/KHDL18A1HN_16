ts = {}

n = int(input("Nhập số thí sinh ban đầu: "))
for _ in range(n):
    sbd = input("Số báo danh: ")
    ten = input("Họ tên: ")
    diem = float(input("Điểm: "))
    ts[sbd] = (ten, diem)

tra = input("Nhập số báo danh cần tra cứu: ")
if tra in ts:
    print("Họ tên:", ts[tra][0], "Điểm:", ts[tra][1])
else:
    ten_moi = input("Không tìm thấy. Nhập tên thí sinh mới: ")
    diem_moi = float(input("Nhập điểm: "))
    ts[tra] = (ten_moi, diem_moi)
    print("Đã thêm thí sinh.")
