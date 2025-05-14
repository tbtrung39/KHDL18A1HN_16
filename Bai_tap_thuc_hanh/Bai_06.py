# Tạo file dữ liệu ban đầu
data = [
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]

with open("bangso.txt", "w") as f:
    for row in data:
        f.write("\t".join(map(str, row)) + "\n")
with open("bangso.txt", "r") as f:
    lines = f.readlines()
    print("Dòng 1:", lines[0].strip())
    print("Dòng 3:", lines[2].strip())
print("Nội dung toàn bộ file:")
with open("bangso.txt", "r") as f:
    for line in f:
        print(line.strip())
# Đọc dữ liệu và xử lý số lẻ
matrix = []
with open("bangso.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.split()))
        row = [str(num) if num % 2 == 1 else '0' for num in nums]
        matrix.append(row)

# Bổ sung dòng nếu thiếu để thành ma trận 4x4
while len(matrix) < 4:
    matrix.append(['0'] * 4)
for row in matrix:
    while len(row) < 4:
        row.append('0')

# Ghi ra file ODD.txt
with open("ODD.txt", "w") as f:
    for row in matrix:
        f.write("\t".join(row) + "\n")
