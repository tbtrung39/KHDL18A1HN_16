import math

def tinh_dien_tich_tam_giac():
    try:
        canh = input("Nhập độ dài 3 cạnh a, b, c (cách nhau bởi dấu cách): ").split()
        if len(canh) != 3:
            raise ValueError("Phải nhập đúng 3 giá trị.")
        
        a, b, c = map(float, canh)

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Các cạnh phải là số dương.")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tạo thành tam giác.")

        p = (a + b + c) / 2
        dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Diện tích tam giác là: {dien_tich:.2f}")

    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception:
        print("Đã xảy ra lỗi không xác định.")
tinh_dien_tich_tam_giac()
