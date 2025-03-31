# Danh sách tuple (name, age, score)
data = [("John", 25, 85), ("Alice", 23, 92), ("Bob", 25, 75), ("Alice", 25, 88)]

# Sắp xếp theo tiêu chí: name -> age -> score (giảm dần)
data.sort(key=lambda x: (x[0], x[1], -x[2]))

# In kết quả
print("Danh sách sau khi sắp xếp:")
for item in data:
    print(item)
