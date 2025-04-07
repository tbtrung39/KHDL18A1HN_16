students = {}
n = int(input("Nhập số lượng sinh viên: "))

for _ in range(n):
    student_id = input("Nhập mã sinh viên (6 ký tự số): ")
    name = input("Nhập tên sinh viên: ")
    score = int(round(float(input("Nhập điểm số: "))))
    students[student_id] = {"name": name, "score": score}

sorted_students = sorted(students.items(), key=lambda x: x[1]["score"], reverse=True)

print("\nDanh sách sinh viên sắp xếp theo điểm giảm dần:")
for student_id, info in sorted_students:
    print(f"Mã: {student_id}, Tên: {info['name']}, Điểm: {info['score']}")