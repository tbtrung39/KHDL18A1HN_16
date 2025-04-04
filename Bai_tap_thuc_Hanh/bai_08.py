import random
A = {42, -15,3.14,-0.001,"hello","xAI",100,2.718,"python"}
print("Tập hợp A:", A)
int_count = 0
float_count = 0
str_count = 0

for element in A:
    if isinstance(element, int) and not isinstance(element, float): 
        int_count += 1
    elif isinstance(element, float):  
        float_count += 1
    elif isinstance(element, str):    
        str_count += 1
print("Số phần tử là số nguyên:", int_count)
print("Số phần tử là số thực:", float_count)
print("Số phần tử là chuỗi ký tự:", str_count)