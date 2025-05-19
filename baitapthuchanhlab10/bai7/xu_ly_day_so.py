import random
import math

def sinh_day_so_ngau_nhien(so_luong_phan_tu=None):
    """Sinh một dãy số ngẫu nhiên có tối đa 100 phần tử."""
    if so_luong_phan_tu is None:
        so_luong_phan_tu = random.randint(1, 100)
    elif not isinstance(so_luong_phan_tu, int) or so_luong_phan_tu <= 0 or so_luong_phan_tu > 100:
        return "Lỗi: Số lượng phần tử phải là số nguyên từ 1 đến 100."
    return [random.randint(1, 1000) for _ in range(so_luong_phan_tu)]

def la_so_nguyen_to(n):
    """Kiểm tra xem một số nguyên dương n có phải là số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    """Liệt kê các số nguyên tố chia hết cho 7 trong dãy số."""
    ket_qua = [num for num in day_so if la_so_nguyen_to(num) and num % 7 == 0]
    return ket_qua

def tinh_tong_so_le(day_so):
    """Tính tổng các số lẻ trong dãy số."""
    return sum(num for num in day_so if num % 2 != 0)

def kiem_tra_so_chinh_phuong(day_so):
    """Kiểm tra xem trong dãy có số chính phương không và trả về danh sách các số đó."""
    so_chinh_phuong = [num for num in day_so if num >= 0 and math.sqrt(num) == int(math.sqrt(num))]
    return so_chinh_phuong

if __name__ == "__main__":
    print("Đây là module xu_ly_day_so. Vui lòng chạy file chương trình chính để sử dụng.")