n = int(input("Nhập số lượng tuple: "))
tuples = []
for _ in range(n):
    name, age, score = input("Nhập name, age, score (cách nhau bởi dấu cách): ").split()
    tuples.append((name, int(age), int(score)))
tuples.sort(key=lambda x: (x[0], x[1], x[2]))
for tup in tuples:
    print(tup)
