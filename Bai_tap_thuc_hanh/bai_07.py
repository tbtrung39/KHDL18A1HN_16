# Tạo danh sách List
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# In danh sách List_
print("Danh sách List_:")
for item in List_:
    print(item)

# Chọn phần tử thứ hai 
selected_value = List_[2][1]
print(f"Phần tử thứ hai trong sublist thứ ba: {selected_value}")

# Kiểm tra độ dài 
import random
if len(List_) < 10:
    new_sublist = ["extra", random.randint(50, 150)]
    List_.append(new_sublist)
    print("Danh sách sau khi thêm phần tử mới:", List_)

# Tính tổng 
total_sales = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print(f"Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật: {total_sales}")
