def ChuvilHinhvuong(a):
    """
    Tính chu vi hình vuông
    """
    return 4 * a
def Dien_tich_hinh_vuong(a):
    """
    Tính diện tích hình vuông
    """
    return a * a
if __name__ == "__main__":
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    print(f"Chu vi hình vuông: {ChuvilHinhvuong(canh)}")
    print(f"Diện tích hình vuông: {Dien_tich_hinh_vuong(canh)}")