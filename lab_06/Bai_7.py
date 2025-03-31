import random

# 1. Tạo danh sách List_ và in ra màn hình
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], 
         ["fri", 115], ["sat", 128], ["sun", 120]]

print("Danh sách List_:")
for item in List_:
    print(item)

# 2. Chọn phần tử thứ hai của sublist ở vị trí thứ 3 (tức là List_[2][1])
third_sublist_second_element = List_[2][1]
print("Phần tử thứ hai của sublist thứ 3:", third_sublist_second_element)

# 3. Kiểm tra độ dài của List_ và thêm một sublist ngẫu nhiên nếu cần
if len(List_) == 7:  # Kiểm tra nếu List_ có 7 phần tử
    random_day = random.choice(["extra1", "extra2", "extra3"])  # Chọn tên ngày ngẫu nhiên
    random_value = random.randint(50, 150)  # Sinh giá trị sale ngẫu nhiên
    List_.append([random_day, random_value])
    print("Danh sách sau khi thêm sublist ngẫu nhiên:", List_)

# 4. Tính tổng sale value trong các ngày thứ hai (mon), thứ ba (tue), thứ bảy (sat) và chủ nhật (sun)
selected_days = ["mon", "tue", "sat", "sun"]
total_sales = sum(value for day, value in List_ if day in selected_days)

print("Tổng sale value của thứ hai, thứ ba, thứ bảy và chủ nhật:", total_sales)