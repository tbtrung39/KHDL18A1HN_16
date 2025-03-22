Str1 = input("Nhập chuỗi Str1: ")
word = ""
for char in Str1:
    if char != ' ' and char != ',':
        word += char
    else:
        if word:
            print(word)
            word = ""
if word:
    print(word)
