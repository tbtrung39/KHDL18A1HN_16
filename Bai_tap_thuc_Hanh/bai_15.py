n = int(input("Nhập số lượng phần tử n: "))
list1 = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]
list2 = [input(f"Nhập tên thứ {i+1}: ") for i in range(n)]

tu_dien = {list1[i]: (list2[i],) for i in range(n)}
print("Từ điển được tạo ra:")
for k, v in tu_dien.items():
    print(f"{k}: {v}")