import random
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# In các phần tử của List
print("Danh sách List:", List)

# Chọn phần tử thứ hai, thuộc vị trí thứ 3 của sublist
phan_tu_thu_hai = List[2][1]
print("Phần tử thứ hai, vị trí thứ 3 của sublist:", phan_tu_thu_hai)

# Kiểm tra độ dài và thêm một sublist ngẫu nhiên
do_dai = len(List)
print("Độ dài của List:", do_dai)
List.append(["random", random.randint(1, 100)])
print("Danh sách List sau khi thêm sublist:", List)

# Tính tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
tong_sale = List[1][1] + List[2][1] + List[5][1] + List[6][1]
print("Tổng sale value:", tong_sale)