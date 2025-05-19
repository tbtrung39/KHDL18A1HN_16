from datetime import date

def tim_tuan_thu_may_trong_nam():
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
    iso_calendar = ngay_da_nhap.isocalendar()
    tuan_thu = iso_calendar[1]
    print(f"\nNgày vừa nhập: {ngay_da_nhap.strftime('%d-%m-%Y')}")
    print(f"Ngày này thuộc tuần thứ {tuan_thu} của năm {iso_calendar[0]}.")
if __name__ == "__main__":
    tim_tuan_thu_may_trong_nam()