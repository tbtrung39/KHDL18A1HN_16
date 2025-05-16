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
        n = input("Nhập số nguyên dương n: ").strip()

        if not n.isdigit():
            raise ValueError("Lỗi: n phải là số nguyên dương.")

        n = int(n)

        if n <= 0:
            raise ValueError("Lỗi: n phải lớn hơn 0.")

        s1 = tong_S1(n)
        s2 = tong_S2(n)

        print(f"S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"S2 = 1² + 2² + ... + {n}² = {s2}")

    except ValueError as ve:
        print(ve)
    except RecursionError:
        print("Lỗi: Quá sâu trong đệ quy! n quá lớn.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

main()