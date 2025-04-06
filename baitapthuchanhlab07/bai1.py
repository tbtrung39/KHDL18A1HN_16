ky_tu_set = set()
print("Nhập các ký tự (nhấn Enter sau mỗi ký tự, nhập 'ESC' để dừng):")
while True:
    ky_tu = input()
    if ky_tu == 'ESC':
        break
    if ky_tu:
        ky_tu_set.add(ky_tu)
print("Set ban đầu:", ky_tu_set)
ky_tu_so = set()
for item in ky_tu_set:
    if item.isdigit():
        ky_tu_so.add(item)
ky_tu_set = ky_tu_set - ky_tu_so
print("Set sau khi xóa ký tự số:", ky_tu_set)