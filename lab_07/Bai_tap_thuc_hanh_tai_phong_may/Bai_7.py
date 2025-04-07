import random

# Nhập dữ liệu từ bàn phím (có thể gồm chữ và số)
data = input("Nhập chuỗi ký tự chữ và số: ")

# Chuyển dữ liệu thành danh sách ký tự duy nhất
unique_chars = list(set(data))

# Đảm bảo có đủ phần tử để tạo 2 tập hợp
if len(unique_chars) < 2:
    print("Chuỗi quá ngắn để tạo 2 tập hợp khác nhau.")
else:
    # Sinh tập hợp A và B với số lượng phần tử ngẫu nhiên từ chuỗi đầu vào
    size_A = random.randint(1, len(unique_chars))
    size_B = random.randint(1, len(unique_chars))

    A = set(random.sample(unique_chars, size_A))
    B = set(random.sample(unique_chars, size_B))

    # Tìm phần tử chung
    common = A.intersection(B)

    # In kết quả
    print("Tập hợp A:", A)
    print("Tập hợp B:", B)
    print("Phần tử chung giữa A và B:", common if common else "Không có phần tử chung.")