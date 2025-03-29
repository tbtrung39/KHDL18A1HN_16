import random
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
# 1. Tạo danh sách List_ và in các phần tử của List_
List_ = List.copy()
print("Danh sách List_:")
for item in List_:
    print(item)

# 2. Chọn ra phần tử thứ hai, thuộc vị trí thứ 3 của sublist
second_element_third_sublist = List[2][1]
print(f"Phần tử thứ hai, thuộc vị trí thứ 3 của sublist: {second_element_third_sublist}")

# 3. Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
test = [["apple", 30], ["banana", 45]]
print(f"Độ dài của danh sách test: {len(test)}")
random_sublist = [random.choice(["orange", "grape", "kiwi"]), random.randint(20, 100)]
test.append(random_sublist)
print(f"Danh sách test sau khi thêm sublist ngẫu nhiên: {test}")

# 4. Tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
sale_values = {
    "mon": 73,
    "tue": 89,
    "sat": 128,
    "sun": 120
}
total_sale_value = sale_values["mon"] + sale_values["tue"] + sale_values["sat"] + sale_values["sun"]
print(f"Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật: {total_sale_value}")
