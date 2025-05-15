import datetime
def main():
    try :
        ngay = int(input("Nhập ngày:"))
        thang = int(input("Nhập tháng :"))
        nam = int(input("Nhập năm:"))
        ngay_duoc_nhap = datetime.date(nam, thang, ngay)
        so_tuan =ngay_duoc_nhap.isocalendar()[1]
        print(f"Ngày {ngay_duoc_nhap.strftime('%d/%m/%Y')} thuộc tuần thứ {so_tuan} trong năm {nam}.")
    
    except ValueError:
        print("Ngày không hợp lệ, vui lòng kiểm tra lại.")
if __name__ == "__main__":
    main()     