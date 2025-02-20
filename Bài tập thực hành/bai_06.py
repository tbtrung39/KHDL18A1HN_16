print('chương trình đọc số nguyên có 3 chữ số :') 
n=int(input('NHập số nguyên 3 chữ sô:')) 
if 100<= n <= 999 or -100<= n <= -999: 
    print('Số nhập vào là số nguyên 3 chữ số:') 
else: 
    print('Số nhập vào không phải số nguyên 3 chữ số:')
hang_tram = n // 100 
hang_chuc = (n // 10) % 10 
hang_dv = n %10 
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  
doc_so="" 
doc_so = doc_so + chu_so[hang_tram] + " trăm" 
if hang_chuc == 0: 
        if hang_dv != 0: 
            doc_so = doc_so + " lẻ " + chu_so[hang_dv] 
elif hang_chuc == 1: 
        if hang_dv == 0: 
            doc_so = doc_so + " mười" 
        elif hang_dv == 5: 
            doc_so = doc_so + " mười lăm" 
        else: 
            doc_so = doc_so + " mười " + chu_so[hang_dv] 
else: 
        doc_so = doc_so + " " + chu_so[hang_chuc] + " mươi" 
        if hang_dv == 1: 
            doc_so = doc_so + " mốt" 
        elif hang_dv == 4: 
            doc_so = doc_so + " tư" 
        elif hang_dv == 5: 
            doc_so = doc_so + " lăm" 
        elif hang_dv != 0: 
            doc_so = doc_so + " " + chu_so[hang_dv] 
print("Số",  n, "được đọc là:", doc_so)             