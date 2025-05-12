import sys
sys.path.append("bai_10\hinhhoc")
import hinhhoc
print("CHUONG TRINH TINH TOAN HINH HOC")
a,b,c=map(int,input("Nhap vao lan luot so do 3 canh cua tam giac: ").split(" "))
if hinhhoc.is_TamGiac(a, b, c):
    print("Ba canh tao thanh mot tam giac.")
    print("Chu vi tam giac la:", hinhhoc.ChuviTamGiac(a, b, c))
    print("Dien tich tam giac la:", hinhhoc.S_TamGiac(a, b, c))
else:
    print("Ba canh khong tao thanh mot tam giac.")

x=int(input("Nhap so do canh hinh vuong: "))
print(f"Chu vi hinh vuong la: {hinhhoc.ChuviHinhvuong(a)}")
print(f"Dien tich hinh vuong la: {hinhhoc.Dien_tich_hinh_vuong(a)}")