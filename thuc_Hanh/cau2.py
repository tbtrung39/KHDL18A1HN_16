Numbers = set()
while True:
    x = input("Nhập số (ESC để kết thúc): ")
    if x.upper() == 'ESC':
        break
    if x.isdigit():
        Numbers.add(int(x))

A = set()
while True:
    x = input("Nhập phần tử tập A (ESC để kết thúc): ")
    if x.upper() == 'ESC':
        break
    if x.isdigit() and int(x) in Numbers:
        A.add(int(x))
print("Tập A:", A)
