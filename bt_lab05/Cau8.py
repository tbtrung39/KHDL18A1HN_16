# Câu 8
#Cach1:
Str = input("Nhập một đoạn văn bản hoàn chỉnh: ")
word = input("Nhập một từ đơn cần tìm: ")
count = Str.split().count(word)
print("Từ '" , word , "' xuất hiện " ,str(count) ," lần trong chuỗi.")
#Cach2:
str = input("Nhập chuỗi văn bản: ")
word = input("Nhập từ đơn: ")
count = 0
word_list = ""
current_word = ""
for char in str:
    if char != ' ':
        current_word += char  
    else:
        if current_word == word:
            count += 1 
        current_word = "" 
if current_word == word:
    count += 1
print("Số lần xuất hiện của từ đơn là:", count)