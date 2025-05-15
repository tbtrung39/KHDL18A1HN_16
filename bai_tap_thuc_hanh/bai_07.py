import datetime
def main():
    try :
        ngay = int(input("Nhập ngày:"))
        thang = int(input("Nhập tháng :"))
        nam = int(input("Nhập năm:"))
        ngay_hien_tai = datetime.date(nam, thang, ngay)
        ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)
        print(f"Ngày kế tiếp : {ngay_ke_tiep.strftime('%d/%m/%Y')}")

    except ValueError:
        print("Ngày không hợp lệ, vui lòng kiểm tra lại.")
if __name__ == "__main__":
    main()     