from datetime import datetime

def main():
    try:
        # Nhập ngày thứ nhất và thứ hai
        ngay1_str = input("Nhập ngày thứ nhất (dd-mm-yyyy): ").strip()
        ngay2_str = input("Nhập ngày thứ hai (dd-mm-yyyy): ").strip()

        # Chuyển chuỗi thành đối tượng datetime
        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")

        # Tính sự khác biệt giữa hai ngày
        delta = abs(ngay2 - ngay1)
        
        # Tính số năm, tháng và ngày
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30

        print(f"Hai ngày cách nhau: {years} năm, {months} tháng, {days} ngày.")
    
    except ValueError:
        print("Lỗi: Định dạng ngày không hợp lệ!")

main()