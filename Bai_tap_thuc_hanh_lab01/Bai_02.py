s = int(input("Nhập giây: "))
m = int(input("Nhập phút: "))
h = int(input("Nhập giờ: "))
d = int(input("Nhập ngày: "))
doi_gia_tri = (d*24*60*60) + (h*60*60) + (m*60) + s
print(doi_gia_tri)