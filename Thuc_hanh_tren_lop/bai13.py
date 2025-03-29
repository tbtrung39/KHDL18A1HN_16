subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]
sentences = [f"{subject} {verb} {obj}" for subject in subjects for verb in verbs for obj in objects]
for sentence in sentences:
    print(sentence)
