import os
print('\n MENU ĐỒ UỐNG')
while True:
    #Hiển thi menu chọn đồ uống
    print('___________________________________________________________________________')
    print("|                          MENU CHỌN ĐỒ UỐNG                              |")
    print("|[1]  CAFE                                                                |")
    print("|[2]  CAM VẮT                                                             |")
    print("|[3]  NƯỚC ÉP CÀ RỐT                                                      |")
    print("|[4]  NƯỚC LỌC                                                            |")
    print("|[5]  NƯỚC DỨA                                                            |")
    print("|[0]  BẤM 0 ĐỂ THOÁT                                                      |")
    print('___________________________________________________________________________')

    chon=int(input("Chọn yêu cầu cần thực hiên."))
    if chon==1:
        print("Bạn đã chọn CAFE.")
    elif chon==2:
        print("Bạn đã chọn CAM VẮT.")
    elif chon==3:
        print("Bạn đã chọn NƯỚC ÉP CÀ RỐT.")
    elif chon==4:
        print("Bạn đã chọn NƯỚC LỌC.")
    elif chon==5:
        print("Bạn đã chọn NƯỚC DỨA.")
    elif chon==0:
        break
    else:
        print("Chỉ được chọn yêu cầu tưd 1-5")
        #break
    tt=input("Nhấn phím bất kì để tiếp tục, bấm số 0 để thoát.")
    if tt==0:
        break
    else: os.system('cls')

