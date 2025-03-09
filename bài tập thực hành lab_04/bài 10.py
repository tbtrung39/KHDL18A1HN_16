chuso = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = int(input("Nhập số: "))
if n == 0:
    print("không")
else:
    ketqua = "" 

    while n > 0:
        chusocuoi = n % 10  
        ket_ua = chuso[chusocuoi] + " " + ketqua  
        n = n // 10  

    print("Kết quả:", ketqua.strip())  