tuples = []
while True:
    data = input("Nhập tuple (name, age, score) hoặc Enter để kết thúc: ")
    if not data:
        break
    name, age, score = data.split(',')
    tuples.append((name.strip(), int(age.strip()), int(score.strip())))
tuples_sorted = sorted(tuples, key=lambda x: (x[0], x[1], x[2]))
print("Tuple sau khi sắp xếp:")
for t in tuples_sorted:
    print(t)