n = int(input("Nhập số lượng phần tử: "))

ds_so = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds_so.append(so)

so_le = list(filter(lambda x: x % 2 != 0, ds_so))

binh_phuong_le = list(map(lambda x: x**2, so_le))

print("\nDanh sách ban đầu:", ds_so)
print("Các số lẻ:", so_le)
print("Bình phương các số lẻ:", binh_phuong_le)
