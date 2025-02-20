d = int(input("Nhập ngày: "))
h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
doi_gia_tri = (d*24*60*60) + (h*60*60) + (m*60) + s
print(doi_gia_tri)