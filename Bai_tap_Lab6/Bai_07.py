List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:")
for sublist in List_:
    print(sublist)
if len(List_) > 2 and len(List_[2]) > 1:
    print("Giá trị của sublist thứ 3:", List_[2][1])
import random
new_sublist = [f"day_{random.randint(1, 10)}", random.randint(50, 150)]
List_.append(new_sublist)
print("Danh sách sau khi thêm:", List_)
days_to_sum = ["mon", "tue", "sat", "sun"]
total_sales = sum(sublist[1] for sublist in List_ if sublist[0] in days_to_sum)
print("Tổng giá trị bán hàng các ngày mon, tue, sat, sun:", total_sales)