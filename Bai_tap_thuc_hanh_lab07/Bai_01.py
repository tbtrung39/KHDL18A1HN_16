import msvcrt

s = set()
print("Nhập các ký tự (ESC để kết thúc): ")
while True:
    ch = msvcrt.getch().decode('utf-8')
    if ch == '\x1b':  # ESC
        break
    print(ch, end=' ')
    s.add(ch)

s2 = set()
for c in s:
    if not c.isdigit():
        s2.add(c)

print("\nTập hợp sau khi loại bỏ ký tự số:", s2)
