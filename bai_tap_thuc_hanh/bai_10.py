from datetime import datetime

def main():
    try:
        ngay1_str = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        ngay2_str = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")

        khoang_cach = abs((ngay2 - ngay1).days)

        nam = khoang_cach // 365
        thang = (khoang_cach % 365) // 30
        ngay = (khoang_cach % 365) % 30
        print(f"Hai ngày cách nhau khoảng: {nam} năm, {thang} tháng, {ngay} ngày.")

    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng ngày (dd-mm-yyyy).")

if __name__ == "__main__":
    main()