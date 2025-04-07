# Khởi tạo set rỗng
char_set = set()

print("Nhập các ký tự (nhập dấu # để kết thúc):")

while True:
    ch = input("Nhập ký tự: ")
    if ch == "#":
        break
    elif len(ch) == 1:  # Đảm bảo là 1 ký tự
        char_set.add(ch)
    else:
        print("Vui lòng chỉ nhập một ký tự!")

# Xóa các ký tự là chữ số
char_set = {c for c in char_set if not c.isdigit()}

# In kết quả
print("Tập hợp sau khi xóa ký tự số:", char_set)