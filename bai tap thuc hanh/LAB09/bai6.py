import random
def tao_hoan_vi_ngau_nhien(n):
    # Tạo dãy A từ 1 đến n
    A = list(range(1, n + 1))
    result = []
    # Lặp qua dãy A và lấy ngẫu nhiên phần tử đưa vào result, sau đó xóa phần tử khỏi A
    while A:
        # Lấy một phần tử ngẫu nhiên từ A
        num = random.choice(A)
        # Thêm vào kết quả
        result.append(num)
        # Xóa phần tử vừa chọn khỏi A
        A.remove(num)
    return result
n = int(input("Nhập số tự nhiên n: "))
print("Hoán vị ngẫu nhiên của các số từ 1 đến", n, "là:", tao_hoan_vi_ngau_nhien(n))