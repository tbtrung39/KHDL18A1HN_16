n = int(input("Nhập số phần tử: "))
lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
binh_phuong = list(map(lambda x: x**2, lst))

print("Danh sách bình phương:", binh_phuong)
