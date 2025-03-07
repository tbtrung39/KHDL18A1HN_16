n = int(input("Nhập n: "))
if n <= 0:
    print("Nhập lại chương trình: ")
else:
    S4 = 0
    bien_khoi_tao = 1
    while bien_khoi_tao <= n:
        S4 += bien_khoi_tao**2
        bien_khoi_tao += 1
    print(S4) 
    S5 = 0
    bien_khoi_tao_1 = 1
    while bien_khoi_tao_1 <= n:
        S5 += bien_khoi_tao_1**3
        bien_khoi_tao_1 +=2
    print(S5)
    S6 = 0
    bien_khoi_tao_3 = 2
    while bien_khoi_tao_3 <= n:
        S6 += bien_khoi_tao_3**4
        bien_khoi_tao_3 += 2
    print(S6)



        