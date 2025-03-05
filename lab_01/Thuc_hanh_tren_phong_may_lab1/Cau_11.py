# Nhập số lần tung xúc sắc
n = int(input("Nhập số lần tung xúc sắc (n): "))

# Xác suất ra 6 cho mỗi xúc sắc
p_3_six = (1 / 6) ** 3  # Xác suất ra 6 cho cả 3 xúc sắc

# Tính xác suất có ít nhất 1 lần cả 3 xúc sắc ra 6 trong n lần
probability = 1 - (1 - p_3_six) ** n

# In kết quả làm tròn đến 2 chữ số thập phân
print(f"Xác suất có ít nhất 1 lần cả 3 xúc sắc ra 6 trong {n} lần tung là: {round(probability, 2)}")