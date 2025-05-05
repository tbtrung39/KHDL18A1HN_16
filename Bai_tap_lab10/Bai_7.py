import random
import math
def generate_and_process():
    """Sinh và xử lý dãy số ngẫu nhiên"""
    numbers = [random.randint(0, 1000) for _ in range(random.randint(50, 100))]
    print("Dãy số:", numbers)
    divisible_by_7 = [x for x in numbers if x % 7 == 0]
    print("Số chia hết cho 7:", divisible_by_7)
    sum_odd = sum(x for x in numbers if x % 2 != 0)
    print("Tổng số lẻ:", sum_odd)
    perfect_squares = [x for x in numbers if math.isqrt(x)**2 == x]
    if perfect_squares:
        print("Số chính phương:", perfect_squares)
    else:
        print("Không có số chính phương")
if __name__ == "__main__":
    generate_and_process()