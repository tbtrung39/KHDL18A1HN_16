# a. Tạo bảng số và ghi vào file
matrix = [
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]
#a
with open("matrix.txt", "w") as f:
    for row in matrix:
        f.write(" ".join(map(str, row)) + "\n")

# b. Hiển thị nội dung dòng đầu tiên và dòng thứ 3
with open("matrix.txt", "r") as f:
    lines = f.readlines()
    print("Dòng đầu tiên:", lines[0].strip())
    print("Dòng thứ ba:", lines[2].strip())

# c. Tìm các số lẻ và ghi vào "ODD.txt" dưới dạng ma trận 4x4
odd_matrix = []
for line in lines:
    row = list(map(int, line.split()))
    odd_row = [num if num % 2 != 0 else 0 for num in row]  # Thay số chẵn bằng 0
    odd_matrix.append(odd_row)

with open("ODD.txt", "w") as f:
    for row in odd_matrix:
        f.write(" ".join(map(str, row)) + "\n")

# d. In ra nội dung dòng cuối của file ODD.txt
with open("ODD.txt", "r") as f:
    odd_lines = f.readlines()
    print("Dòng cuối của ODD.txt:", odd_lines[-1].strip())