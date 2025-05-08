#a
with open("Bài_tập_thực_Hành/so.txt", "r") as f:
    lines = f.readlines()
    print("Dòng đầu tiên:", lines[0].strip())
    print("Dòng thứ ba:", lines[2].strip())

#b
print("\n Toàn bộ nội dung so.txt")
with open("Bài_tập_thực_Hành/so.txt", "r") as f:
    print(f.read())
#c
numbers = []
with open("Bài_tập_thực_Hành/so.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        numbers.extend(nums)

odd_matrix = []
for i in range(4):
    row = []
    for j in range(4):
        idx = i * 4 + j
        if idx < len(numbers):
            val = numbers[idx]
            row.append(str(val) if val % 2 == 1 else "0")
        else:
            row.append("0")
    odd_matrix.append(row)

with open("Bài_tập_thực_Hành/ODD.txt", "w") as f:
    for row in odd_matrix:
        f.write(" ".join(row) + "\n")

#d
with open("Bài_tập_thực_Hành/ODD.txt", "r") as f:
    lines = f.readlines()
    print("Dòng cuối trong ODD.txt:")
    print(lines[-1].strip())