print("Nhập đoạn văn (2 lần Enter để kết thúc):")
lines=[]
while True:
    line = input()
    if line =="":
        break
    lines.append(line)
Str= "".join(line)
word = input("Nhập từ đơn cần tìm:").strip()
words_list = Str.split()
count = words_list.count(word)
print("Từ" ,word, "xuất hiện" ,count, "lần trong đoạn văn",)