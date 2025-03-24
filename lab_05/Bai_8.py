import re

# Nhập đoạn văn bản từ bàn phím (có thể nhập nhiều dòng)
print("Nhập đoạn văn bản (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

Str = " ".join(lines)  # Ghép các dòng thành một đoạn văn bản

# Nhập từ đơn cần tìm
word = input("Nhập từ đơn cần tìm: ").strip().lower()  # Chuẩn hóa về chữ thường

# Loại bỏ dấu câu để đếm chính xác
Str_cleaned = re.sub(r"[^\w\s]", "", Str).lower()

# Cách 1: Dùng công thức với split() và count()
words_list1 = Str_cleaned.split()  # Tách thành danh sách các từ
count1 = words_list1.count(word)  # Đếm số lần xuất hiện của từ
print(f"Số lần xuất hiện của '{word}' (cách 1):", count1)

# Cách 2: Dùng vòng lặp để tách từ và đếm thủ công
count2 = 0
words_list2 = []
word_temp = ""

for char in Str_cleaned:
    if char.isalnum():  # Nếu là chữ cái hoặc số, thêm vào từ tạm
        word_temp += char
    else:
        if word_temp:  # Nếu có từ đang lưu, thêm vào danh sách
            words_list2.append(word_temp)
            word_temp = ""

if word_temp:  # Nếu còn từ cuối cùng
    words_list2.append(word_temp)

# Đếm số lần xuất hiện thủ công
for w in words_list2:
    if w == word:
        count2 += 1

print(f"Số lần xuất hiện của '{word}' (cách 2):", count2)