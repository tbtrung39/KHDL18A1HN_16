import math 
print("Chương trình giải phương trình bậc 2: ") 
a,b,c = map(float,input("Nhập hệ số a,b,c: ").split()) 
if a == 0: 
    if b == 0: 
        if c == 0: 
            print("Phương trình có vô số nghiệm.") 
        else: 
            print("Phương trình vô nghiệm.") 
    else: 
        x = -c / b 
        print(f"Phương trình có một nghiệm duy nhất: x = {x:.2f}") 
else: 
    delta = b**2 - 4*a*c 
    print(f"Giá trị Δ (Delta) = {delta:.2f}") 
    if delta > 0: 
        x1 = (-b + math.sqrt(delta)) / (2 * a) 
        x2 = (-b - math.sqrt(delta)) / (2 * a) 
        print(f"Phương trình có hai nghiệm phân biệt:") 
        print(f"x1 = {x1:.2f}") 
        print(f"x2 = {x2:.2f}") 
    elif delta == 0: 
        x = -b / (2 * a) 
        print(f"Phương trình có nghiệm kép: x = {x:.2f}") 
    else: 
        x1=-b+math.sqrt(abs(delta)) / (2 * a) 
        x2=-b-math.sqrt(abs(delta)) / (2 * a) 
        print(f'Phương trình có 2 nghiệm phức : x1={x1:.2f},x2={x2:.2f}') 