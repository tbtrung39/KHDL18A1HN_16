lst = []
while True:
    num = int(input("Nhập một số tự nhiên (hoặc 0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)

# 1. Chuyển các phần tử dương lên đầu danh sách
positive = [x for x in lst if x > 0]
non_positive = [x for x in lst if x <= 0]
lst = positive + non_positive
print(f"Danh sách sau khi chuyển các phần tử dương lên đầu: {lst}")

# 2. Chèn một số m vào đầu, cuối và vị trí thứ 5 của danh sách
m = int(input("Nhập số m: "))
lst.insert(0, m)
lst.append(m)
if len(lst) >= 5:
    lst.insert(5, m)
else:
    lst.append(m)

print(f"Danh sách sau khi chèn số m: {lst}")
