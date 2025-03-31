subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]

sentences = [f"{s} {v} {o}" for s in subjects for v in verbs for o in objects]
for sentence in sentences:
    print(sentence)