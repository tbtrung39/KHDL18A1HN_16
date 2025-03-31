import random
# Tạo danh sách List_ và in các phần tử của List_
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for item in List_:
    print(item)

# Chọn phần tử thứ hai, thuộc vị trí thứ 3 củacủa sublist
phantu = List_[2][1]
print("Phần tử thứ hai của sublist thứ 3:", phantu)

# Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
test = List_[:]
print("Độ dài ban đầu của test:", len(test))
sublist_moi = ["extra", random.randint(50, 150)]
test.append(sublist_moi)
print("Danh sách sau khi thêm phần tử:", test)

# Tính tổng sale value của các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
tong_sale = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng sale value:", tong_sale)