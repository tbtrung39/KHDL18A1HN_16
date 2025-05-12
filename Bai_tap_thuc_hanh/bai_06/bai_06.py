with open(r"Bai_tap_thuc_hanh\bai_06\input.txt", "r") as f:
    lines = f.readlines()

#a,
print("a. Dòng đầu tiên:", lines[0].strip())
print("   Dòng thứ 3:", lines[2].strip())
#b,
print("\nb. Toàn bộ nội dung file:")
for line in lines:
    print(line.strip())

# c.
odd_matrix = []
for line in lines[1:]:  
    row = []
    for num in line.strip().split():
        number = int(num)
        if number % 2 == 1:
            row.append(str(number))
        else:
            row.append("0")
    odd_matrix.append(row)

with open("ODD.txt", "w") as f:
    for row in odd_matrix:
        f.write(" ".join(row) + "\n")

# d.
with open("ODD.txt", "r") as f:
    odd_lines = f.readlines()
    print("\nd. Dòng cuối cùng của file ODD.txt:")
    print(odd_lines[-1].strip())