char_set = set()
print("Nhập các ký tự (gõ liên tiếp, Enter để kết thúc):")
chuoi = input()
for c in chuoi:
    char_set.add(c)
char_set = {c for c in char_set if not c.isdigit()}
print("Tập hợp sau khi xóa ký tự số:", char_set)