n=int(input("Nhap vao so lan tung xuc xac: ")) 
p_khong_co = (1-(1/6)**3)**n 
p_it_nhat_mot = 1 - p_khong_co 
print("Xac suat it nhat mot lan ca 3 vien ra 6: %0.2f"%p_it_nhat_mot)