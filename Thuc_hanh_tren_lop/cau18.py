students = {
    "123456": {"name": "Alice", "score": 8},
    "234567": {"name": "Bob", "score": 7},
    "345678": {"name": "Charlie", "score": 9}
}
exam_id = input("Nhập số báo danh: ")
if exam_id in students:
    print(f"Họ và tên: {students[exam_id]['name']}, Điểm thi: {students[exam_id]['score']}")
else:
    name = input("Nhập họ và tên thí sinh: ")
    score = float(input("Nhập điểm thi của thí sinh: "))
    students[exam_id] = {"name": name, "score": round(score)}
    print(f"Thông tin thí sinh đã được thêm: Mã số: {exam_id}, Họ và tên: {name}, Điểm thi: {round(score)}")