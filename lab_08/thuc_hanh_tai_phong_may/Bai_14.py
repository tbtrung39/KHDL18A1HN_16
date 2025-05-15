n = int(input("Nhập số lượng phần tử n: "))

# Nhập n số nguyên vào list
lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

# Tạo list bình phương dùng map và lambda
lst_binh_phuong = list(map(lambda x: x**2, lst))

print("Danh sách bình phương các số đã nhập là:")
print(lst_binh_phuong)