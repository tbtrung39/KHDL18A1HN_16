n = int(input("Nhập số lượng phần tử n: "))

lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

# Lọc số lẻ, sau đó lấy bình phương
lst_le_binh_phuong = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lst)))

print("Danh sách bình phương các số lẻ là:")
print(lst_le_binh_phuong)