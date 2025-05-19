from datetime import date, timedelta

def tim_ngay_ke_tiep():
    while True:
        try:
            ngay = int(input("Nhập ngày (1-31): "))
            thang = int(input("Nhập tháng (1-12): "))
            nam = int(input("Nhập năm : "))
            try:
                ngay_da_nhap = date(nam, thang, ngay)
                break 
            except ValueError:
                print("Lỗi: Ngày, tháng, năm không hợp lệ. Vui lòng nhập lại.")

        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên cho ngày, tháng, năm.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")
    ngay_ke_tiep = ngay_da_nhap + timedelta(days=1)
    print(f"\nNgày vừa nhập: {ngay_da_nhap.strftime('%d-%m-%Y')}")
    print(f"Ngày kế tiếp là: {ngay_ke_tiep.strftime('%d-%m-%Y')}")
if __name__ == "__main__":
    tim_ngay_ke_tiep()