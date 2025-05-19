def nhap_so_nguyen():
    while True:
        try:
            so_nguyen = int(input("Vui lòng nhập một số nguyên: "))
            return so_nguyen
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

def sang_nhi_phan(n):
    """Chuyển đổi số nguyên n sang hệ nhị phân (binary)."""
    return bin(n)[2:]  

def sang_bat_phan(n):
    """Chuyển đổi số nguyên n sang hệ bát phân (octal)."""
    return oct(n)[2:] 

def sang_thap_luc_phan(n):
    """Chuyển đổi số nguyên n sang hệ thập lục phân (hexadecimal)."""
    return hex(n)[2:].upper() 

if __name__ == "__main__":
    print("Đây là module doicoso1. Vui lòng chạy file chương trình chính để sử dụng.")