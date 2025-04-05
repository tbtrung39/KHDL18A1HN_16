def sum_common_digits(m, n):
    m_str = str(m)
    n_str = str(n)
    common_digits = set(m_str) & set(n_str)
    total_sum = sum(int(digit) for digit in common_digits)
    return total_sum
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
result = sum_common_digits(m, n)
print(f"Tổng các chữ số chung của {m} và {n} là: {result}")