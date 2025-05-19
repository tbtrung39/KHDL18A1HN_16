def tinh_s1_de_quy(n):
    """Tính tổng S1 = 1 + 2 + ... + n bằng đệ quy."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Giá trị n phải là một số nguyên dương.")
    if n == 1:
        return 1
    else:
        return n + tinh_s1_de_quy(n - 1)
def tinh_s2_de_quy(n):
    """Tính tổng S2 = 1² + 2² + 3² + ... + n² bằng đệ quy."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Giá trị n phải là một số nguyên dương.")
    if n == 1:
        return 1
    else:
        return n**2 + tinh_s2_de_quy(n - 1)
def main():
    while True:
        try:
            n_str = input("Vui lòng nhập một số nguyên dương n: ")
            n = int(n_str)
            if n <= 0:
                raise ValueError("Giá trị n phải là một số nguyên dương.")

            s1 = tinh_s1_de_quy(n)
            s2 = tinh_s2_de_quy(n)

            print(f"Với n = {n}:")
            print(f"S1 = 1 + 2 + ... + {n} = {s1}")
            print(f"S2 = 1² + 2² + ... + {n}² = {s2}")
            break  

        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()