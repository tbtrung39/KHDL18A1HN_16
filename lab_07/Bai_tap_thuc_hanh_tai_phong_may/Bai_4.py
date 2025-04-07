# Danh sách chiều cao của các sinh viên
heights = [161, 162, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 
           145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 
           169, 168, 167, 170]

# a. Đếm số sinh viên
num_students = len(heights)

# b. Tính chiều cao trung bình
average_height = sum(heights) / num_students

# c. Liệt kê các chiều cao khác nhau và tính chiều cao trung bình của nhóm
unique_heights = sorted(set(heights))  # set() để loại bỏ chiều cao trùng lặp, sorted() để sắp xếp

# In kết quả
print(f"a. Nhóm có {num_students} sinh viên.")
print(f"b. Chiều cao trung bình của các sinh viên trong nhóm là: {average_height:.2f} cm.")
print(f"c. Các chiều cao khác nhau trong nhóm: {unique_heights}")
print(f"   Chiều cao trung bình của nhóm: {average_height:.2f} cm.")