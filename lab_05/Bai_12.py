import re

# Nhập chuỗi từ bàn phím
Str1 = input("Nhập chuỗi Str1: ")

# Cách 1: Dùng công thức với re.split()
words1 = re.split(r'[ ,]+', Str1.strip())  # Tách bằng khoảng trắng hoặc dấu phẩy
print("Các từ trong chuỗi (cách 1):")
for word in words1:
    print(word)

# Cách 2: Dùng vòng lặp để tách từ thủ công
words2 = []
word = ""

for char in Str1:
    if char.isalnum() or char in "áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựíìỉĩịýỳỷỹỵđ":  # Ký tự hợp lệ
        word += char
    else:
        if word:  # Nếu đã có từ, thêm vào danh sách
            words2.append(word)
            word = ""

if word:  # Nếu còn từ cuối cùng
    words2.append(word)

print("Các từ trong chuỗi (cách 2):")
for w in words2:
    print(w)