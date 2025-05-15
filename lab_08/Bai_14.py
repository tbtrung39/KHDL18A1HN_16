n = int(input("Nhập số lượng phần tử: "))

ds_so = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds_so.append(so)

ds_binh_phuong = list(map(lambda x: x**2, ds_so))

print("\nDanh sách ban đầu:", ds_so)
print("Danh sách bình phương:", ds_binh_phuong)
