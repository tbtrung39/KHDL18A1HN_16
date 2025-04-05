m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))
if m < 0 or n < 0:
    print("m và n phải là số tự nhiên (>= 0)!")
else:
    m_str = str(m)
    n_str = str(n)
    digits_m = set()
    digits_n = set()

    i = 0
    while i < len(m_str):
        digits_m.add(m_str[i])
        i += 1
    j = 0
    while j < len(n_str):
        digits_n.add(n_str[j])
        j += 1
    common_digits = digits_m & digits_n

    total = 0
    for digit in common_digits:
        total += int(digit)
    print("Các chữ số chung:", common_digits)
    print("Tổng các chữ số chung:", total)