s = set()
while True:
    x = input("Nhập phần tử (ESC để kết thúc): ")
    if x.upper() == 'ESC':
        break
    s.add(x)
print("Tập hợp:", s)
