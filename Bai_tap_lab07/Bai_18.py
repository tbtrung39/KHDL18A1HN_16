candidates = {
    "001": {"name": "Nguyen Van A", "score": 8},
    "002": {"name": "Tran Thi B", "score": 7},
}

candidate_id = input("Nhập số báo danh: ")

if candidate_id in candidates:
    print(f"Thông tin thí sinh: Tên: {candidates[candidate_id]['name']}, Điểm: {candidates[candidate_id]['score']}")
else:
    print("Thí sinh không tồn tại. Thêm thông tin mới.")
    name = input("Nhập họ và tên: ")
    score = float(input("Nhập điểm thi: "))
    candidates[candidate_id] = {"name": name, "score": score}
    print("Thí sinh đã được thêm vào từ điển.")