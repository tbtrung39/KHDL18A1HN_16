data = []
while True:
    user_input = input("Nhập (tên, tuổi, điểm) hoặc nhấn Enter để kết thúc: ")
    if user_input == "":  
        break  
    try:
        name, age, score = user_input.split(",")  
        name = name.strip()  
        age = int(age.strip())  
        score = int(score.strip())  
        data.append((name, age, score))
    except ValueError:
        print("Lỗi! Vui lòng nhập đúng định dạng: tên, tuổi, điểm")
data.sort(key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sách sau khi sắp xếp:")
for item in data:
    print(item)