n = int(input("Nhập số lượng sinh viên: "))
students = {}

for _ in range(n):
    student_id = input("Nhập mã sinh viên (6 ký tự số): ")
    name = input("Nhập tên sinh viên: ")
    score = round(float(input("Nhập điểm số (0-10): ")))
    score = max(0, min(score, 10)) 
    students[student_id] = {'name': name, 'score': score}
for student_id, info in sorted(students.items(), key=lambda x: x[1]['score'], reverse=True):
    print(f"Mã sinh viên: {student_id}, Tên: {info['name']}, Điểm: {info['score']}")