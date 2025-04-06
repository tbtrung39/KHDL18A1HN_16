m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
m_digits = set(str(m))
n_digits = set(str(n))
common_digits = set()
for digit in m_digits:
    if digit in n_digits:
        common_digits.add(digit)
total = 0
for digit in common_digits:
    total += int(digit)
print("Tổng các chữ số chung:", total)