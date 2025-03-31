# Danh sách tuple đầu vào (name, age, score)
data = [
    ("Linh", 20, 85.5),
    ("An", 22, 90.0),
    ("Binh", 20, 78.0),
    ("An", 20, 88.0),
    ("Linh", 19, 92.5),
    ("Binh", 22, 80.0)
]

# Sắp xếp theo (name, age, score)
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

# In danh sách đã sắp xếp
for item in sorted_data:
    print(item)