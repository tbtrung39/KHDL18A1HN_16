from datetime import datetime

def tinh_khoang_cach_ngay(ngay1_str, ngay2_str):
    try:
        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")
    except ValueError:
        return None

    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1  

    nam_khac = ngay2.year - ngay1.year
    thang_khac = ngay2.month - ngay1.month
    ngay_khac = ngay2.day - ngay1.day

    if ngay_khac < 0:
        thang_khac -= 1
        thang_truoc = ngay2.month - 1
        if thang_truoc == 0:
            thang_truoc = 12
        so_ngay_thang_truoc = (datetime(ngay2.year, thang_truoc + 1, 1) - datetime(ngay2.year, thang_truoc, 1)).days
        ngay_khac += so_ngay_thang_truoc

    if thang_khac < 0:
        nam_khac -= 1
        thang_khac += 12

    return nam_khac, thang_khac, ngay_khac

ngay_thu_nhat_str = input("Nhập ngày tháng năm thứ nhất theo định dạng dd-mm-yyyy: ")
ngay_thu_hai_str = input("Nhập ngày tháng năm thứ hai theo định dạng dd-mm-yyyy: ")

khoang_cach = tinh_khoang_cach_ngay(ngay_thu_nhat_str, ngay_thu_hai_str)

if khoang_cach:
    nam, thang, ngay = khoang_cach
    print(f"Khoảng cách giữa {ngay_thu_nhat_str} và {ngay_thu_hai_str} là: {nam} năm, {thang} tháng, {ngay} ngày.")
else:
    print("Định dạng ngày không hợp lệ. Vui lòng nhập theo định dạng dd-mm-yyyy.")
    