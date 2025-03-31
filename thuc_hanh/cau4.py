numbers = []
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break
    numbers.append(n)

numbers.insert(1, [1, 2, 3])  # Chèn vào vị trí thứ 2
numbers.insert(5, 5)  # Chèn vào vị trí thứ 6
k = int(input("Nhập vị trí cần xóa: "))
if 0 <= k < len(numbers):
    numbers.pop(k)

sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)

print("Danh sách sau khi xử lý:", numbers)
print("Sắp xếp tăng dần:", sorted_asc)
print("Sắp xếp giảm dần:", sorted_desc)
