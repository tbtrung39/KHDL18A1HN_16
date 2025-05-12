def filter_hex_chars(s):
    """Lọc ký tự hợp lệ cho hệ hex"""
    valid_chars = set("0123456789ABCDEFabcdef")
    return ''.join(c for c in s if c in valid_chars)
def determine_base(s):
    """Xác định cơ số của chuỗi số"""
    if set(s) <= set("01"):
        return 2
    elif set(s) <= set("01234567"):
        return 8
    elif set(s) <= set("0123456789ABCDEFabcdef"):
        return 16
    return 0
def convert_to_decimal(s, base):
    """Chuyển từ hệ cơ số base sang hệ 10"""
    return int(s, base)
if __name__ == "__main__":
    s = input("Nhập chuỗi số: ")
    filtered = filter_hex_chars(s)
    print("Chuỗi sau lọc:", filtered)
    
    base = determine_base(filtered)
    print("Cơ số phát hiện:", base)
    
    if base > 0:
        print("Giá trị thập phân:", convert_to_decimal(filtered, base))