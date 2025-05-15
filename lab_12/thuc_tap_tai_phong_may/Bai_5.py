def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return n**2 + tong_S2(n - 1)

def main():
    try:
        n = input("Nhập số nguyên dương n: ")
        
        # Kiểm tra kiểu dữ liệu
        if not n.isdigit():
            raise ValueError("Lỗi: Bạn phải nhập một số nguyên dương.")

        n = int(n)

        # Kiểm tra giá trị hợp lệ
        if n <= 0:
            raise ValueError("Lỗi: n phải lớn hơn 0.")

        # Gọi hàm đệ quy
        s1 = tong_S1(n)
        s2 = tong_S2(n)

        # In kết quả
        print(f"S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"S2 = 1^2 + 2^2 + ... + {n}^2 = {s2}")

    except ValueError as ve:
        print(ve)
    except RecursionError:
        print("Lỗi: Số quá lớn gây tràn ngăn xếp đệ quy!")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}")

# Gọi hàm chính
main()