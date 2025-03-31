# Danh sách chủ ngữ, động từ và tân ngữ
subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các câu bằng cách kết hợp chủ ngữ, động từ và tân ngữ
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}")
