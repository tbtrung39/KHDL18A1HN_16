
n=int(input("Nhap so sinh vien: "))
c=set(input("Nhap danh sach sinh vien thi C++(cach nhau boi khoang trang): ").split())
java=set(input("Nhap danh sach sinh vien thi Java(cach nhau boi khoang trang): ").split())
python=set(input("Nhap danh sach sinh vien thi Python(cach nhau boi khoang trang): ").split())

chi_thi_mot_ngon_ngu=(c-java-python).union(java-c-python).union(python-c-java)
thi_hai_ngon_ngu=(c.intersection(java)).union(c.intersection(python)).union(java.intersection(python))
dru_thi_tat_ca=c.intersection(java).intersection(python)

print("Sinh vien chi thi mot ngon ngu:",chi_thi_mot_ngon_ngu)
print("Sinh vien thi hai ngon ngu:",thi_hai_ngon_ngu)
print("Sinh vien du thi tat ca ba ngon ngu:",dru_thi_tat_ca)
