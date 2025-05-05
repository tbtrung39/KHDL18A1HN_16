def convert_number_systems():
    """Chuyển đổi số giữa các hệ cơ số"""
    n = int(input("Nhập số nguyên: "))
    print(f"Số vừa nhập: {n}")
    print(f"Nhị phân: {bin(n)}")
    print(f"Bát phân: {oct(n)}")
    print(f"Thập lục phân: {hex(n)}")
if __name__ == "__main__":
    convert_number_systems()