# Danh sách chủ ngữ, động từ, tân ngữ
subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các câu có thể bằng List Comprehension
sentences = [f"{subj} {verb} {obj}" for subj in subjects for verb in verbs for obj in objects]

# In danh sách câu
for sentence in sentences:
    print(sentence)