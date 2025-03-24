str = """Buoi sang mat troi moc, chieu nhung tia nang vang xuong canh dong.
Tieng chim hot vang len, hoa la lung lay trong con gio nhe.  h
Nguoi dan lang bat dau mot ngay moi voi nhung viec quen thuoc."""
nhap = input("Nhập từ muốn tìm: ")
dem = 0
for i in str:
    if nhap == i:
        dem += 1
print(dem)
