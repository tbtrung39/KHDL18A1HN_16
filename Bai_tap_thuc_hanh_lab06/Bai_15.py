# Nhập số lượng tuple
n = int(input("Nhập số lượng tuple: "))

# Khởi tạo danh sách để lưu các tuple
tuples = []

# Nhập các tuple từ người dùng
for _ in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    tuples.append((name, age, score))

# Sắp xếp danh sách các tuple theo thứ tự name, age, score
tuples.sort(key=lambda x: (x[0], x[1], x[2]))

# In danh sách sau khi sắp xếp
print("Danh sách sau khi sắp xếp:")
for item in tuples:
    print(item)
