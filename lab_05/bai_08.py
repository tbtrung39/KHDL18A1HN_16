str="Cuoc song giong nhu mot dong song, luc em dem phang lang, luc lai cuon trao du doi." \
" Co nhung ngay nang dep, ta cam thay moi thu deu thuan loi, nhung cung co nhung ngay bao giong, thu thach cu ap den lien tuc. " \
"Quan trong la ta chon cach doi mat the nao, tron tranh hay kien cuong vuot qua. " \
"Vi sau tat ca, mua roi cung tanh, bau troi lai trong xanh nhu chua tung co giong bao."
print("Cho doan van: Cuoc song giong nhu mot dong song, luc em dem phang lang, luc lai cuon trao du doi." \
" Co nhung ngay nang dep, ta cam thay moi thu deu thuan loi, nhung cung co nhung ngay bao giong, thu thach cu ap den lien tuc. " \
"Quan trong la ta chon cach doi mat the nao, tron tranh hay kien cuong vuot qua. " \
"Vi sau tat ca, mua roi cung tanh, bau troi lai trong xanh nhu chua tung co giong bao.")
n=input("Nhap vao mot tu don: ").lower()
tu_don=str.split()
dem=tu_don.count(n)
print(f"So lan xuat hien cua tu '{n}' trong doan van la:",dem)