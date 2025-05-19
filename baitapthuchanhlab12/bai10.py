from datetime import date

def tinh_khoang_cach_giua_hai_ngay():
    def nhap_ngay(thu_tu):
        while True:
            try:
                ngay_str = input(f"Nhập ngày thứ {thu_tu} theo định dạng dd-mm-yyyy: ")
                ngay_obj = date.strptime(ngay_str, '%d-%m-%Y')
                return ngay_obj
            except ValueError:
                print("Lỗi: Định dạng ngày không hợp lệ. Vui lòng nhập theo định dạng dd-mm-yyyy.")
            except Exception as e:
                print(f"Đã xảy ra lỗi không mong muốn: {e}")

    ngay1 = nhap_ngay(1)
    ngay2 = nhap_ngay(2)

    if ngay1 > ngay2:
        ngay_dau = ngay2
        ngay_sau = ngay1
        dau_lon_hon_sau = True
    else:
        ngay_dau = ngay1
        ngay_sau = ngay2
        dau_lon_hon_sau = False

    nam_khac = ngay_sau.year - ngay_dau.year
    thang_khac = ngay_sau.month - ngay_dau.month
    ngay_khac = ngay_sau.day - ngay_dau.day

    if ngay_khac < 0:
        thang_khac -= 1
        if ngay_dau.month == 1:
            thang_truoc = 12
            nam_khac -= 1
        else:
            thang_truoc = ngay_dau.month - 1
        so_ngay_thang_truoc = (date(ngay_dau.year + (1 if thang_truoc == 12 else 0), thang_truoc + 1, 1) - date(ngay_dau.year + (1 if thang_truoc == 12 else 0), thang_truoc, 1)).days
        ngay_khac += so_ngay_thang_truoc

    if thang_khac < 0:
        nam_khac -= 1
        thang_khac += 12

    print(f"\nNgày thứ nhất: {ngay1.strftime('%d-%m-%Y')}")
    print(f"Ngày thứ hai: {ngay2.strftime('%d-%m-%Y')}")

    if dau_lon_hon_sau:
        print(f"Hai ngày này cách nhau: {nam_khac} năm, {thang_khac} tháng, {ngay_khac} ngày (ngày thứ nhất sau ngày thứ hai).")
    else:
        print(f"Hai ngày này cách nhau: {nam_khac} năm, {thang_khac} tháng, {ngay_khac} ngày.")

if __name__ == "__main__":
    tinh_khoang_cach_giua_hai_ngay()