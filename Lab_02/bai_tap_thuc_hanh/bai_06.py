so = int(input("Nhập vào số nguyên có ba chữ số: "))

hang_tram = so // 100
hang_chuc = (so // 10) % 10
hang_don_vi = so % 10

cach_doc = {
    0: "không",
    1: "một",
    2: "hai",
    3: "ba",
    4: "bốn",
    5: "năm",
    6: "sáu",
    7: "bảy",
    8: "tám",
    9: "chín"
}

print(f"{cach_doc[hang_tram]} trăm {cach_doc[hang_chuc]} mươi {cach_doc[hang_don_vi]}")