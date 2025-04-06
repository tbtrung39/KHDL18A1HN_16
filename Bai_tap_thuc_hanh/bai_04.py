heights_str = "161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163 162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170"
heights_list = heights_str.split()
heights = []
for height_str in heights_list:
    heights.append(int(height_str))

num_students = len(heights)
print("Số lượng sinh viên:", num_students)

total_height = 0
for height in heights:
    total_height += height
average_height = total_height / num_students
print("Chiều cao trung bình:", average_height)

unique_heights = set()
for height in heights:
    unique_heights.add(height)

print("Các chiều cao khác nhau:", unique_heights)