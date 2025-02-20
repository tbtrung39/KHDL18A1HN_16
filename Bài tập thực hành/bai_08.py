print('chương trình tính lương của nhân viên dựa theo thâm niên công tác') 
lcb=1350000 
tntc=int(input('Nhập số tháng:')) 
if tntc < 12: 
    hso=2.34 
elif 12 <= tntc < 36: 
    hso=3.33 
elif 36 <= tntc < 60: 
    hso=3.66 
else : 
    hso=3.99 
luong=hso*lcb 
print('Lương của nhân viên là:',luong) 