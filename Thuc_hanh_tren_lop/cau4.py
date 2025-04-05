# Danh sách chiều cao của các sinh viên
heights = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 
           162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

# a. Hỏi nhóm có bao nhiêu sinh viên?
num_students = len(heights)
print(f"Số lượng sinh viên trong nhóm: {num_students}")

# b. Tính chiều cao trung bình của các sinh viên trong nhóm
average_height = sum(heights) / num_students
print(f"Chiều cao trung bình của các sinh viên: {average_height:.2f}")

# c. Liệt kê các chiều cao khác nhau sinh viên trong nhóm và in ra chiều cao trung bình
unique_heights = sorted(set(heights))  
print(f"Các chiều cao khác nhau của sinh viên: {unique_heights}")