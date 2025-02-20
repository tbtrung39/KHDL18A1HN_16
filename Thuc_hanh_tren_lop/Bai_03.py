PI = 3.14
# Nhập bán kính và chiều cao
r = float(input("Nhập bán kính của khối trụ (r): "))
h = float(input("Nhập chiều cao của khối trụ (h): "))

# Diện tích xung quanh
A_xungquanh = 2 * PI * r * h

# Diện tích toàn phần
A_toanphan = 2 * PI * r * h + 2 * PI * r**2

# Thể tích khối trụ
V = PI * r**2 * h

# In kết quả, làm tròn đến 2 chữ số thập phân
print(f"Diện tích xung quanh của khối trụ là: {A_xungquanh:.2f}")
print(f"Diện tích toàn phần của khối trụ là: {A_toanphan:.2f}")
print(f"Thể tích của khối trụ là: {V:.2f}")