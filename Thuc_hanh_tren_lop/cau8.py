Str = input("Nhập đoạn văn bản: ")
word = input("Nhập từ đơn cần tìm: ")
count = Str.split().count(word)
print(f"Từ '{word}' xuất hiện {count} lần.")
